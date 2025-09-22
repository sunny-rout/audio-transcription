import os
from tkinter import Tk, filedialog
import shutil

# ---------------------------
# Copy file Operations
# ---------------------------
def copy_file_to_local(source_path: list, dest_dir: str = "uploads"):
    """
    Copies a file to a local directory.

    Args:
        source_path (str): The path to the source file.
        dest_dir (str): The destination directory. Defaults to "uploads".

    Returns:
        str: The path to the copied file in the local directory.
    """
    os.makedirs(dest_dir, exist_ok=True)
    dest_paths = []
    for path in source_path:
        base_filename = os.path.basename(path)
        dest_path = os.path.join(dest_dir, base_filename)
        dest_paths.append(dest_path)
        try:
            shutil.copy(path, dest_path)
            print(f"File copied to '{dest_path}'")
        except IOError as e:
            print(f"Error copying file: {e}")

    return dest_paths


# ---------------------------
# File Picker (if no arg)
# ---------------------------
def select_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(
        title="Select an audio file",
        filetypes=[("Audio Files", "*.mp3 *.wav *.flac *.aac *.m4a"), ("All Files", "*.*")]
    )
    return copy_file_to_local(list(file_paths))


# ---------------------------
# Delete existing audio files
# ---------------------------
def clear_audio_files(folder="uploads", extensions=(".mp3", ".wav", ".flac", ".aac", ".m4a")):
    """Deletes files with specified extensions from a folder."""
    if not os.path.isdir(folder):
        print(f"Warning: Directory '{folder}' not found. Skipping cleanup.")
        return

    try:
        for entry in os.scandir(folder):
            if entry.is_file() and entry.name.endswith(extensions):
                os.remove(entry.path)
    except OSError as e:
        print(f"Error during file cleanup in '{folder}': {e}")


def save_transcription(input_file, text, output_dir="output"):
    """Save transcription to output folder"""
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_dir, f"{base_name}.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Transcription saved as: {output_file}")

    clear_audio_files()  # Clean up audio files after saving transcription
