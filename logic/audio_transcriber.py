import subprocess
import os
import uuid

async def transcribe_audio(audio_file):
    # Save the uploaded audio file to disk
    temp_filename = f"temp_{uuid.uuid4()}.wav"
    with open(temp_filename, "wb") as f:
        f.write(await audio_file.read())

    try:
        # Run whisper CLI command
        result = subprocess.run(
            ["whisper", temp_filename, "--model", "base", "--output_format", "txt"],
            check=True,
            capture_output=True,
            text=True
        )

        # Read the output transcription from generated file
        txt_filename = temp_filename.replace(".wav", ".txt")
        with open(txt_filename, "r", encoding="utf-8") as f:
            transcription = f.read()

        return transcription.strip()

    except subprocess.CalledProcessError as e:
        print("Whisper failed:", e.stderr)
        return "Sorry, I couldn't transcribe the audio."

    finally:
        # Clean up temp files
        os.remove(temp_filename)
        txt_path = temp_filename.replace(".wav", ".txt")
        if os.path.exists(txt_path):
            os.remove(txt_path)
