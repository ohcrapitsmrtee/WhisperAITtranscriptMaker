# 🎙️ WhisperAI Transcript Maker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI Whisper](https://img.shields.io/badge/Powered%20by-OpenAI%20Whisper-green.svg)](https://github.com/openai/whisper)

A powerful and user-friendly tool for transcribing audio files (MP3, WAV, etc.) to text using OpenAI's Whisper model. Perfect for transcribing voicemails, meetings, interviews, or any speech recordings!

![Demo Screenshot](https://via.placeholder.com/600x400/2d3748/ffffff?text=GUI+Application+Screenshot)

## ✨ Features

- 🖥️ **GUI Application**: Easy drag-and-drop interface for transcribing audio files
- 🎯 **Multiple Model Sizes**: Choose from tiny, base, small, medium, or large Whisper models
- 📁 **Batch Processing**: Transcribe multiple files at once
- 💾 **Multiple Output Formats**: Save as text files, JSON, or copy to clipboard
- 🎵 **Supported Audio Formats**: MP3, WAV, M4A, FLAC, OGG, AAC
- ⚡ **No Manual Text File Opening**: View transcriptions directly in the interface
- 🔄 **Background Processing**: Non-blocking transcription with progress indicators

## 🚀 Quick Start

### Option 1: GUI Application (Recommended)
```bash
# 1. Clone the repository
git clone https://github.com/ohcrapitsmrtee/WhisperAITtranscriptMaker.git
cd WhisperAITtranscriptMaker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the GUI
python transcription_app.py
```

### Option 2: One-Click Setup (Windows)
```bash
# Run the setup script
python setup.py

# Launch with batch file
start_transcription_tool.bat
```

## 📱 Usage

### 🖥️ GUI Application (Main Interface)

Launch the graphical interface:
```bash
python transcription_app.py
```

**Simple Steps:**
1. 🤖 **Select Model**: Choose "base" for best speed/accuracy balance
2. ⚡ **Load Model**: Click "Load Model" (downloads ~74MB first time)
3. 📂 **Choose File**: Browse for your MP3, WAV, or other audio file
4. 🎯 **Transcribe**: Click "Transcribe Audio" and wait for results
5. 📝 **Get Results**: View transcript directly in the app
6. 💾 **Save/Copy**: Save to file, copy to clipboard, or clear

### 💻 Command Line Interface

#### Single File Transcription
```bash
# Basic usage
python transcribe_cli.py audio_file.mp3

# With options
python transcribe_cli.py voicemail.wav --model medium --format console
python transcribe_cli.py meeting.mp3 --output transcript.txt
```

#### Batch Processing
```bash
# Process all audio files in a folder
python batch_transcribe.py --folder ./audio_files --output ./transcripts

# Process specific files
python batch_transcribe.py --files file1.mp3 file2.wav --model small
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

## 🎯 Use Cases

### Perfect for:
- 📞 **Voicemail transcription**
- 🎤 **Meeting recordings**
- 🎙️ **Interview transcriptions**
- 📱 **Voice memos**
- 🎓 **Lecture recordings**
- 📻 **Podcast content**
- 🗣️ **Accessibility needs**

### Real Examples:
```bash
# Transcribe voicemails
python transcribe_cli.py voicemail_mom.mp3 --format console

# Batch process meeting recordings
python batch_transcribe.py --folder ./meetings --model medium

# High-accuracy interview transcription
python transcribe_cli.py interview.wav --model large --output interview_transcript.txt
```

## 📦 Installation

### Prerequisites
- **Python 3.8+** 
- **Internet connection** (for model download)
- **~1GB free space** (for models)

### Quick Install
```bash
git clone https://github.com/ohcrapitsmrtee/WhisperAITtranscriptMaker.git
cd WhisperAITtranscriptMaker
pip install -r requirements.txt
python transcription_app.py
```

### Manual Install
```bash
pip install git+https://github.com/openai/whisper.git
pip install pydub torch torchaudio
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

## 📊 Model Comparison

| Model    | Size     | Speed    | Accuracy | Memory | Best For |
|----------|----------|----------|----------|--------|----------|
| `tiny`   | ~39 MB   | ⚡⚡⚡    | ⭐⭐     | Low    | Quick tests, real-time |
| `base`   | ~74 MB   | ⚡⚡      | ⭐⭐⭐   | Low    | **General use** 🏆 |
| `small`  | ~244 MB  | ⚡       | ⭐⭐⭐⭐ | Med    | Important files |
| `medium` | ~769 MB  | 🐌       | ⭐⭐⭐⭐⭐| High   | Professional use |
| `large`  | ~1550 MB | 🐌🐌     | ⭐⭐⭐⭐⭐| High   | Critical accuracy |

## 🔧 Tools Overview

| Tool | Purpose | Usage |
|------|---------|--------|
| `transcription_app.py` | **🖥️ Main GUI** | Launch with Python or double-click |
| `transcribe_cli.py` | **📄 Single files** | `python transcribe_cli.py file.mp3` |
| `batch_transcribe.py` | **📁 Multiple files** | `python batch_transcribe.py --folder ./audio` |
| `test_tool.py` | **🧪 Test suite** | `python test_tool.py` |
| `setup.py` | **⚙️ Installation** | `python setup.py` |

## 🛠️ Troubleshooting

<details>
<summary>🔍 Click to expand troubleshooting guide</summary>

### Common Issues:

#### "No module named 'whisper'"
```bash
pip install git+https://github.com/openai/whisper.git
# or
python setup.py
```

#### Slow transcription
- Use smaller model: `--model tiny` or `--model base`
- Check available RAM and CPU
- Close other applications

#### Audio file not supported
- Install FFmpeg for more formats
- Convert to MP3 or WAV: 
  ```bash
  ffmpeg -i input.m4a output.wav
  ```

#### Out of memory errors
- Use `tiny` or `base` model
- Transcribe shorter files (< 30 minutes)
- Close other applications

#### GUI won't start
```bash
# Test installation
python test_tool.py --check

# Use CLI instead
python transcribe_cli.py your_file.mp3
```

</details>

## ⚡ Performance Tips

- **🏆 Best Balance**: Use `base` model for most tasks
- **🎵 Audio Quality**: Higher quality = better accuracy
- **⏱️ File Length**: Works best with < 30 minute files
- **💻 Hardware**: GPU acceleration automatic with CUDA
- **🔇 Noise**: Clean audio gives better results

## 🎵 Supported Formats

| Format | Extension | Quality | Notes |
|--------|-----------|---------|-------|
| MP3    | `.mp3`    | Good    | Most common |
| WAV    | `.wav`    | Best    | Uncompressed |
| M4A    | `.m4a`    | Good    | Apple format |
| FLAC   | `.flac`   | Best    | Lossless |
| OGG    | `.ogg`    | Good    | Open source |
| AAC    | `.aac`    | Good    | Compressed |

## 📄 License

This project is open source and uses OpenAI's Whisper model. Please check OpenAI's license and usage terms for Whisper.

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- 🐛 Submit bug reports
- 💡 Suggest new features  
- 🔧 Submit pull requests
- 📖 Improve documentation
- ⭐ Star this repository if you find it helpful!

## 🙏 Acknowledgments

- **OpenAI** for the incredible Whisper model
- **Python community** for amazing libraries
- **Contributors** who help improve this tool

---

Made with ❤️ for easy audio transcription
