
import sys
import os
from utils.audio import convert_to_wav, transcribe_audio
from utils.files import save_transcription

def main():
    # Ensure user provided an audio file
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/audiofile")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    print(f"Processing file: {input_file}")

    # Convert to WAV format if needed
    wav_file = convert_to_wav(input_file)

    # Run transcription
    text = transcribe_audio(wav_file)

    # Save transcription
    save_transcription(input_file, text)

    print("✅ Transcription complete! Check the 'output/' folder.")

if __name__ == "__main__":
    main()
