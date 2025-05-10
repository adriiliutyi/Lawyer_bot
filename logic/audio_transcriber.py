import whisper

model = whisper.load_model("base")

async def transcribe_audio(audio_file):
    contents = await audio_file.read()
    with open("temp_audio.wav", "wb") as f:
        f.write(contents)
    result = model.transcribe("temp_audio.wav")
    return result["text"]
