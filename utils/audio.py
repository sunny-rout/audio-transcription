import os
import whisper
from pydub import AudioSegment

def convert_to_wav(input_file):
    """
    Converts any audio format (mp3, m4a, wav, etc.) to wav format
    using pydub. Returns the path of the converted wav file.
    """
    filename, _ = os.path.splitext(os.path.basename(input_file))
    wav_file = f"{filename}.wav"

    audio = AudioSegment.from_file(input_file)
    audio.export(wav_file, format="wav")

    return wav_file


def transcribe_audio(wav_file):
    """
    Uses OpenAI Whisper model to transcribe audio into text.
    """
    print("Transcribing... (this may take a while for large files)")
    model = whisper.load_model("base")  # options: tiny, base, small, medium, large
    result = model.transcribe(wav_file)
    return result["text"]
