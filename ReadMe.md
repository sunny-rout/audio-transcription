# Audio Transcriber 🎤➡️📝

A simple Python project that takes any audio file (`.mp3`, `.wav`, `.m4a`, etc.) and transcribes it into text using Whisper.

---

## Features
- Supports multiple audio formats (`.mp3`, `.wav`, `.m4a`, etc.)
- Converts audio automatically to `.wav` if needed
- Uses [OpenAI Whisper](https://github.com/openai/whisper) for transcription
- Saves results into the `output/` folder as `.txt` files
- Beginner-friendly project structure

---

## Setup

### 1. Clone the project
```bash
git clone https://github.com/your-username/audio-transcriber.git
cd audio-transcriber
```
### 2. Create a virtual environment & install requirements

```bash
python -m venv venv

# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate\

pip install -r requirements.txt
```

#### Install FFmpeg
Whisper and pydub need FFmpeg to handle audio.

#### Windows:

- Download the latest static build from FFmpeg Builds
- Extract it (e.g., to C:\ffmpeg).
- Add C:\ffmpeg\bin to your PATH:
    - Press Win + R, type sysdm.cpl.
    - Go to Advanced > Environment Variables.
    - Edit Path → Add C:\ffmpeg\bin.
- Restart your terminal and check:
```powershell
ffmpeg -version
```

**Linux/Mac:**
```bash
sudo apt-get install ffmpeg   # Ubuntu/Debian
brew install ffmpeg           # Mac (Homebrew)
```

### 4. Install PyTorch (required by Whisper)

#### CPU-only version (works everywhere):
```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
```
#### GPU version (optional, if you have CUDA):
Follow instructions here: https://pytorch.org/get-started/locally/


### 5. Configure the Transcriber (Optional)

You can edit the `config.yaml` file to change default settings:
```yaml
# Default configuration for Audio Transcriber

model: "base"          # tiny, base, small, medium, large
language: "en"         # auto or specify language code
output_dir: "output"
log_level: "INFO"      # DEBUG, INFO, WARNING, ERROR
chunk_duration: 300    # in seconds (for large files)
```

## Usage

#### Transcribe a single file:
```
python main.py path/to/audiofile.mp3
```

#### Transcribe multiple file:
```
python main.py path/to/audiofile.mp3, path/to/audiofile2.mp3
```
The transcription will be saved in the output/ folder as a `.txt` file.