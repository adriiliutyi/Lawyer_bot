from gtts import gTTS

def text_to_audio(text, user_id):
    tts = gTTS(text)
    path = f"{user_id}_response.mp3"
    tts.save(path)
    return path
