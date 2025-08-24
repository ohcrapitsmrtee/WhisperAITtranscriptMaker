#!/usr/bin/env python3
"""
Command-line Speech-to-Text Transcription Tool
Simple CLI tool for transcribing audio files using OpenAI Whisper
"""

import argparse
import whisper
import os
import sys
from pathlib import Path

def transcribe_audio(file_path, model_size="base", output_format="txt", output_file=None):
    """
    Transcribe an audio file using Whisper
    
    Args:
        file_path (str): Path to the audio file
        model_size (str): Whisper model size to use
        output_format (str): Output format (txt, json, or console)
        output_file (str): Optional output file path
    """
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return False
    
    try:
        print(f"Loading Whisper model: {model_size}")
        model = whisper.load_model(model_size)
        
        print(f"Transcribing: {os.path.basename(file_path)}")
        result = model.transcribe(file_path)
        
        transcript = result["text"].strip()
        
        if output_format == "console":
            print("\n" + "="*50)
            print("TRANSCRIPTION")
            print("="*50)
            print(transcript)
            print("="*50)
        
        elif output_format == "txt":
            if output_file is None:
                # Generate output filename based on input file
                input_path = Path(file_path)
                output_file = input_path.with_suffix('.txt')
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(transcript)
            print(f"Transcript saved to: {output_file}")
        
        elif output_format == "json":
            import json
            if output_file is None:
                input_path = Path(file_path)
                output_file = input_path.with_suffix('.json')
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"Full results saved to: {output_file}")
        
        return True
        
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        return False

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="Transcribe audio files using OpenAI Whisper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python transcribe_cli.py audio.mp3
  python transcribe_cli.py audio.wav --model medium --output transcript.txt
  python transcribe_cli.py voicemail.mp3 --format console
        """
    )
    
    parser.add_argument(
        "file", 
        help="Path to the audio file to transcribe"
    )
    
    parser.add_argument(
        "--model", 
        choices=["tiny", "base", "small", "medium", "large"],
        default="base",
        help="Whisper model size to use (default: base)"
    )
    
    parser.add_argument(
        "--format",
        choices=["txt", "json", "console"],
        default="txt",
        help="Output format (default: txt)"
    )
    
    parser.add_argument(
        "--output", "-o",
        help="Output file path (optional, auto-generated if not specified)"
    )
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.isfile(args.file):
        print(f"Error: '{args.file}' is not a valid file.")
        sys.exit(1)
    
    # Transcribe
    success = transcribe_audio(
        args.file, 
        args.model, 
        args.format, 
        args.output
    )
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
