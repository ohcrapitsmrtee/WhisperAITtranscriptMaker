#!/usr/bin/env python3
"""
Setup and Installation Helper
Automates the setup process for the Speech-to-Text Transcription Tool
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    print(f"Running: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed")
        print(f"Error: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False

def check_python():
    """Check Python version"""
    print("Checking Python version...")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("✗ Python 3.8 or higher is required")
        return False
    
    print("✓ Python version is compatible")
    return True

def setup_environment():
    """Setup the Python environment and install packages"""
    print("\n" + "="*50)
    print("SPEECH-TO-TEXT TRANSCRIPTION TOOL SETUP")
    print("="*50)
    
    # Check Python
    if not check_python():
        return False
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing Python packages"):
        print("\nTrying alternative installation method...")
        commands = [
            "pip install git+https://github.com/openai/whisper.git",
            "pip install pydub",
            "pip install torch torchaudio"
        ]
        
        for cmd in commands:
            if not run_command(cmd, f"Installing {cmd.split()[-1]}"):
                print(f"Failed to install {cmd.split()[-1]}")
                return False
    
    # Test import
    print("\nTesting Whisper installation...")
    try:
        import whisper
        print("✓ Whisper imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Whisper: {e}")
        return False
    
    print("\n" + "="*50)
    print("SETUP COMPLETE!")
    print("="*50)
    print("\nYou can now run:")
    print("1. GUI Application: python transcription_app.py")
    print("2. Command Line: python transcribe_cli.py audio_file.mp3")
    print("3. Batch Processing: python batch_transcribe.py --folder audio_folder")
    print("\nSee README.md for detailed usage instructions.")
    
    return True

def main():
    """Main setup function"""
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        # Just check the installation
        print("Checking installation...")
        try:
            import whisper
            print("✓ Whisper is installed and ready")
        except ImportError:
            print("✗ Whisper is not installed. Run: python setup.py")
            return
        
        try:
            import tkinter
            print("✓ Tkinter (GUI) is available")
        except ImportError:
            print("⚠ Tkinter not available - GUI won't work, but CLI will")
        
        print("Installation check complete!")
        return
    
    # Full setup
    setup_environment()

if __name__ == "__main__":
    main()
