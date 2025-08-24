@echo off
echo Starting Speech-to-Text Transcription Tool...
echo.
echo Make sure you have:
echo 1. Installed requirements: pip install -r requirements.txt
echo 2. Audio files ready (MP3, WAV, etc.)
echo.
pause
echo Loading GUI application...
"%~dp0.venv\Scripts\python.exe" "%~dp0transcription_app.py"
pause
