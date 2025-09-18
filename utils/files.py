import os

def save_transcription(input_file, text):
    """
    Saves transcription text into the output/ folder
    with the same base name as the input file.
    """
    os.makedirs("output", exist_ok=True)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join("output", f"{base_name}.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Transcription saved as: {output_file}")
