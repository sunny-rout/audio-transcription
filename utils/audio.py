import os
from pydub import AudioSegment

def convert_to_wav(input_file):
    """Converts any audio format to .wav"""
    filename, _ = os.path.splitext(os.path.basename(input_file))
    wav_file = f"{filename}.wav"
    audio = AudioSegment.from_file(input_file)
    audio.export(wav_file, format="wav")
    return wav_file

def split_audio(wav_file, chunk_duration=300):
    """Split audio into smaller chunks for large files"""
    audio = AudioSegment.from_wav(wav_file)
    chunks = []
    for i in range(0, len(audio), chunk_duration * 1000):  # ms
        chunk = audio[i:i + chunk_duration * 1000]
        chunk_file = f"{os.path.splitext(wav_file)[0]}_part{i//1000}.wav"
        chunk.export(chunk_file, format="wav")
        chunks.append(chunk_file)
    return chunks
