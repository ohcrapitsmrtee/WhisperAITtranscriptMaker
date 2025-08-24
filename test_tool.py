#!/usr/bin/env python3
"""
Quick Test Script
Test the transcription tools with a sample or user-provided audio file
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from pathlib import Path

def test_cli_transcription():
    """Test the CLI transcription tool"""
    print("Testing CLI transcription...")
    
    # Ask user to select an audio file
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    file_path = filedialog.askopenfilename(
        title="Select an audio file to test transcription",
        filetypes=[
            ('Audio files', '*.mp3 *.wav *.m4a *.flac *.ogg'),
            ('All files', '*.*')
        ]
    )
    
    if not file_path:
        print("No file selected. Exiting.")
        return False
    
    print(f"Selected file: {file_path}")
    
    # Test CLI transcription
    python_exe = sys.executable
    cli_script = Path(__file__).parent / "transcribe_cli.py"
    
    cmd = [python_exe, str(cli_script), file_path, "--format", "console"]
    
    print("Running CLI transcription...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✓ CLI transcription successful!")
            print("\nOutput:")
            print(result.stdout)
        else:
            print("✗ CLI transcription failed!")
            print("Error:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("✗ Transcription timed out (5 minutes)")
        return False
    except Exception as e:
        print(f"✗ Error running transcription: {e}")
        return False
    
    return True

def check_installation():
    """Check if all components are installed"""
    print("Checking installation...")
    
    try:
        import whisper
        print("✓ Whisper is installed")
    except ImportError:
        print("✗ Whisper is not installed")
        print("Run: pip install git+https://github.com/openai/whisper.git")
        return False
    
    try:
        import tkinter
        print("✓ Tkinter is available (GUI will work)")
    except ImportError:
        print("⚠ Tkinter not available (GUI won't work, but CLI will)")
    
    try:
        import pydub
        print("✓ Pydub is installed")
    except ImportError:
        print("⚠ Pydub not installed (may affect some audio formats)")
    
    # Check if scripts exist
    scripts = ["transcription_app.py", "transcribe_cli.py", "batch_transcribe.py"]
    for script in scripts:
        if os.path.exists(script):
            print(f"✓ {script} found")
        else:
            print(f"✗ {script} missing")
    
    return True

def main():
    """Main test function"""
    print("="*50)
    print("SPEECH-TO-TEXT TRANSCRIPTION TOOL - TEST UTILITY")
    print("="*50)
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--check":
            check_installation()
            return
        elif sys.argv[1] == "--test":
            if check_installation():
                test_cli_transcription()
            return
    
    print("\nWhat would you like to do?")
    print("1. Check installation")
    print("2. Test CLI transcription with an audio file")
    print("3. Launch GUI application")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            check_installation()
            
        elif choice == "2":
            if check_installation():
                test_cli_transcription()
            
        elif choice == "3":
            print("Launching GUI application...")
            try:
                python_exe = sys.executable
                gui_script = Path(__file__).parent / "transcription_app.py"
                subprocess.Popen([python_exe, str(gui_script)])
                print("GUI application started!")
            except Exception as e:
                print(f"Failed to launch GUI: {e}")
            
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
