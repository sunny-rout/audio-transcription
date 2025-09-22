import whisper

def transcribe_audio(wav_file, model_size="base", language="en"):
    """Transcribes audio using Whisper"""
    model = whisper.load_model(model_size)
    result = model.transcribe(wav_file, language=None if language == "auto" else language)
    return result["text"]
