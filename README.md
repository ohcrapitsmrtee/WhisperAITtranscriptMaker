# Speech-to-Text Transcription Tool

A powerful and user-friendly tool for transcribing audio files (MP3, WAV, etc.) to text using OpenAI's Whisper model. Features both a graphical interface and command-line tools.

## Features

- **GUI Application**: Easy drag-and-drop interface for transcribing audio files
- **Multiple Model Sizes**: Choose from tiny, base, small, medium, or large Whisper models
- **Batch Processing**: Transcribe multiple files at once
- **Multiple Output Formats**: Save as text files, JSON, or copy to clipboard
- **Supported Audio Formats**: MP3, WAV, M4A, FLAC, OGG, AAC
- **No Manual Text File Opening**: View transcriptions directly in the interface

## Installation

1. **Clone or download this repository**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install git+https://github.com/openai/whisper.git
   pip install pydub torch torchaudio
   ```

3. **FFmpeg (Optional but recommended):**
   - For better audio format support, install FFmpeg
   - You already have FFmpeg in this workspace at: `ffmpeg-2025-01-08-git-251de1791e-essentials_build/bin/`

## Usage

### 1. GUI Application (Recommended)

Launch the graphical interface:
```bash
python transcription_app.py
```

**Steps:**
1. Select a Whisper model size (base recommended for most use cases)
2. Click "Load Model" to initialize the AI model
3. Browse and select your audio file (MP3, WAV, etc.)
4. Click "Transcribe Audio" and wait for the transcription
5. View the transcript in the text area
6. Save to file, copy to clipboard, or clear as needed

**Model Size Guide:**
- **tiny**: Fastest, lower accuracy (~39 MB)
- **base**: Good balance of speed and accuracy (~74 MB) - **Recommended**
- **small**: Better accuracy, slower (~244 MB)
- **medium**: High accuracy (~769 MB)
- **large**: Best accuracy, slowest (~1550 MB)

### 2. Command Line Interface

For single file transcription:
```bash
python transcribe_cli.py audio_file.mp3
```

**Options:**
```bash
python transcribe_cli.py audio_file.mp3 --model medium --format console
python transcribe_cli.py voicemail.wav --output transcript.txt
python transcribe_cli.py recording.mp3 --format json --output results.json
```

### 3. Batch Processing

Process multiple files in a folder:
```bash
python batch_transcribe.py --folder ./audio_files --output ./transcripts
```

Process specific files:
```bash
python batch_transcribe.py --files file1.mp3 file2.wav file3.mp3 --model medium
```

## File Structure

```
SpeechToTextTranscriptMaker/
├── transcription_app.py      # Main GUI application
├── transcribe_cli.py         # Command-line single file tool
├── batch_transcribe.py       # Batch processing tool
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── ffmpeg-*/                # FFmpeg binaries (optional)
```

## Examples

### Transcribing a Voicemail
1. Save your voicemail as an MP3 or WAV file
2. Run the GUI app: `python transcription_app.py`
3. Load the "base" model
4. Select your voicemail file
5. Click "Transcribe Audio"
6. Copy the text or save to a file

### Batch Processing Voice Memos
```bash
python batch_transcribe.py --folder ./voice_memos --model base --output ./transcripts
```

### Quick Console Output
```bash
python transcribe_cli.py important_meeting.mp3 --format console
```

## Troubleshooting

### Common Issues:

1. **"No module named 'whisper'"**
   - Make sure you installed the requirements: `pip install -r requirements.txt`

2. **Slow transcription**
   - Use a smaller model (tiny or base)
   - Ensure you have sufficient RAM and CPU

3. **Audio file not supported**
   - Install FFmpeg for better audio format support
   - Convert your audio to MP3 or WAV format

4. **Out of memory errors**
   - Use a smaller model size (tiny or base)
   - Try transcribing shorter audio files

### Performance Tips:

- **Model Selection**: Start with "base" model for best speed/accuracy balance
- **Audio Quality**: Higher quality audio = better transcription accuracy
- **File Size**: Whisper works best with files under 30 minutes
- **Hardware**: GPU acceleration is automatic if CUDA is available

## Model Comparison

| Model  | Size   | Speed | Accuracy | Best For |
|--------|--------|-------|----------|----------|
| tiny   | ~39 MB | Fast  | Good     | Quick tests, real-time |
| base   | ~74 MB | Good  | Very Good| General use (recommended) |
| small  | ~244 MB| Slow  | Better   | Important transcriptions |
| medium | ~769 MB| Slower| High     | Professional use |
| large  | ~1550 MB| Slowest| Best    | Critical accuracy needed |

## Supported Audio Formats

- MP3 (most common)
- WAV (uncompressed)
- M4A (Apple)
- FLAC (lossless)
- OGG (open source)
- AAC (compressed)

## License

This project uses OpenAI's Whisper model. Please check their license and usage terms.

## Contributing

Feel free to submit issues or pull requests to improve this tool!
