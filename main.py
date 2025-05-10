from fastapi import FastAPI, UploadFile, Form
from logic.audio_transcriber import transcribe_audio
from logic.question_flow import get_next_question
from logic.response_generator import generate_legal_advice
from logic.tts import text_to_audio

app = FastAPI()

sessions = {}

@app.post("/ask")
async def ask_lawyer(user_id: str = Form(...), user_input: str = Form(None), audio: UploadFile = None):
    if user_id not in sessions:
        sessions[user_id] = []

    # Handle audio
    if audio:
        user_input = await transcribe_audio(audio)

    sessions[user_id].append({"user": user_input})

    next_q = get_next_question(sessions[user_id])
    if next_q:
        sessions[user_id].append({"bot": next_q})
        return {"reply": next_q}

    final_answer = generate_legal_advice(sessions[user_id])
    sessions[user_id].append({"bot": final_answer})

    audio_file_path = text_to_audio(final_answer, user_id)
    return {"reply": final_answer, "audio": audio_file_path}
