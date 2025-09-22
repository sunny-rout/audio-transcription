
import argparse
import os
import yaml

from utils.audio import convert_to_wav, split_audio
from utils.transcription import transcribe_audio
from utils.file_ops import save_transcription, select_file
from utils.logger import get_logger
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load configuration from config.yaml
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

logger = get_logger(config.get("log_level", "INFO"))

def parse_args():
    parser = argparse.ArgumentParser(description="Audio Transcriber using Whisper")
    parser.add_argument("input_file", nargs="?", default="", help="Path to input audio file")
    parser.add_argument("--model", default=config["model"], help="Whisper model size (tiny, base, small, medium, large)")
    parser.add_argument("--language", default=config["language"], help="Language code or 'auto'")
    parser.add_argument("--output", default=config["output_dir"], help="Output directory for transcripts")
    return parser.parse_args()

def main():
    # Ensure user provided an audio file
    args = parse_args()

    input_files = []
    if args.input_file and ',' in args.input_file:
        input_files = args.input_file.split(',')
    elif args.input_file:
        input_files.append(args.input_file)

    if len(input_files) == 0:
        input_files = select_file()

    for input_file in input_files:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found.")
            return

        logger.info(f"Processing file: {input_file}")

        # Convert to wav
        wav_file = convert_to_wav(input_file)
        
        # Chunking if audio is too long
        chunks = split_audio(wav_file, chunk_duration=config["chunk_duration"])
        logger.info(f"Audio split into {len(chunks)} chunks.")

        # Transcribe each chunk
        full_text = ""
        for idx, chunk in enumerate(chunks, 1):
            logger.info(f"Transcribing chunk {idx}/{len(chunks)}...")
            text = transcribe_audio(chunk, model_size=args.model, language=args.language)
            full_text += text + "\n"
            os.remove(chunk)  # Clean up chunk file


        # Save transcription
        save_transcription(input_file, full_text, args.output)
        os.remove(wav_file)  # Clean up wav file
        
        logger.info("✅ Transcription complete for file: {input_file.name}")

        
    logger.info("✅ Transcription complete!")

if __name__ == "__main__":
    main()
