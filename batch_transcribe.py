#!/usr/bin/env python3
"""
Batch Audio Transcription Tool
Process multiple audio files at once using OpenAI Whisper
"""

import os
import glob
import whisper
from pathlib import Path
import time
import argparse

class BatchTranscriber:
    def __init__(self, model_size="base"):
        """Initialize batch transcriber with specified model"""
        print(f"Loading Whisper model: {model_size}")
        self.model = whisper.load_model(model_size)
        self.model_size = model_size
        
    def transcribe_folder(self, folder_path, output_dir=None, file_pattern="*"):
        """
        Transcribe all audio files in a folder
        
        Args:
            folder_path (str): Path to folder containing audio files
            output_dir (str): Directory to save transcripts (optional)
            file_pattern (str): File pattern to match (e.g., "*.mp3")
        """
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' not found.")
            return
        
        # Supported audio extensions
        audio_extensions = ['.mp3', '.wav', '.m4a', '.flac', '.ogg', '.aac']
        
        # Find audio files
        audio_files = []
        folder_path = Path(folder_path)
        
        for ext in audio_extensions:
            pattern = file_pattern.replace('*', f'*{ext}')
            audio_files.extend(folder_path.glob(pattern))
        
        if not audio_files:
            print(f"No audio files found in '{folder_path}' matching pattern '{file_pattern}'")
            return
        
        # Create output directory if specified
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        else:
            output_dir = folder_path
        
        print(f"Found {len(audio_files)} audio files to transcribe")
        print(f"Output directory: {output_dir}")
        print("-" * 50)
        
        successful = 0
        failed = 0
        start_time = time.time()
        
        for i, audio_file in enumerate(audio_files, 1):
            print(f"[{i}/{len(audio_files)}] Processing: {audio_file.name}")
            
            try:
                # Transcribe
                result = self.model.transcribe(str(audio_file))
                transcript = result["text"].strip()
                
                # Save transcript
                output_file = output_dir / f"{audio_file.stem}_transcript.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"File: {audio_file.name}\n")
                    f.write(f"Model: {self.model_size}\n")
                    f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("-" * 40 + "\n\n")
                    f.write(transcript)
                
                print(f"  ✓ Saved to: {output_file.name}")
                successful += 1
                
            except Exception as e:
                print(f"  ✗ Failed: {str(e)}")
                failed += 1
            
            print()
        
        # Summary
        total_time = time.time() - start_time
        print("=" * 50)
        print("BATCH TRANSCRIPTION COMPLETE")
        print("=" * 50)
        print(f"Total files processed: {len(audio_files)}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Total time: {total_time:.2f} seconds")
        print(f"Average time per file: {total_time/len(audio_files):.2f} seconds")
    
    def transcribe_file_list(self, file_list, output_dir=None):
        """
        Transcribe a list of specific files
        
        Args:
            file_list (list): List of file paths to transcribe
            output_dir (str): Directory to save transcripts (optional)
        """
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"Processing {len(file_list)} files")
        print(f"Output directory: {output_dir or 'Same as input files'}")
        print("-" * 50)
        
        successful = 0
        failed = 0
        start_time = time.time()
        
        for i, file_path in enumerate(file_list, 1):
            file_path = Path(file_path)
            
            if not file_path.exists():
                print(f"[{i}/{len(file_list)}] ✗ File not found: {file_path}")
                failed += 1
                continue
            
            print(f"[{i}/{len(file_list)}] Processing: {file_path.name}")
            
            try:
                result = self.model.transcribe(str(file_path))
                transcript = result["text"].strip()
                
                # Determine output file path
                if output_dir:
                    output_file = output_dir / f"{file_path.stem}_transcript.txt"
                else:
                    output_file = file_path.parent / f"{file_path.stem}_transcript.txt"
                
                # Save transcript
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"File: {file_path.name}\n")
                    f.write(f"Model: {self.model_size}\n")
                    f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("-" * 40 + "\n\n")
                    f.write(transcript)
                
                print(f"  ✓ Saved to: {output_file}")
                successful += 1
                
            except Exception as e:
                print(f"  ✗ Failed: {str(e)}")
                failed += 1
            
            print()
        
        # Summary
        total_time = time.time() - start_time
        print("=" * 50)
        print("BATCH TRANSCRIPTION COMPLETE")
        print("=" * 50)
        print(f"Total files processed: {len(file_list)}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Total time: {total_time:.2f} seconds")
        if len(file_list) > 0:
            print(f"Average time per file: {total_time/len(file_list):.2f} seconds")

def main():
    """Main CLI function for batch processing"""
    parser = argparse.ArgumentParser(
        description="Batch transcribe audio files using OpenAI Whisper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python batch_transcribe.py --folder ./audio_files
  python batch_transcribe.py --folder ./voicemails --model medium --output ./transcripts
  python batch_transcribe.py --files file1.mp3 file2.wav file3.mp3
        """
    )
    
    parser.add_argument(
        "--folder",
        help="Folder containing audio files to transcribe"
    )
    
    parser.add_argument(
        "--files",
        nargs='+',
        help="List of specific audio files to transcribe"
    )
    
    parser.add_argument(
        "--model",
        choices=["tiny", "base", "small", "medium", "large"],
        default="base",
        help="Whisper model size to use (default: base)"
    )
    
    parser.add_argument(
        "--output", "-o",
        help="Output directory for transcripts (optional)"
    )
    
    parser.add_argument(
        "--pattern",
        default="*",
        help="File pattern to match when using --folder (default: *)"
    )
    
    args = parser.parse_args()
    
    if not args.folder and not args.files:
        parser.error("Either --folder or --files must be specified")
    
    # Initialize transcriber
    transcriber = BatchTranscriber(args.model)
    
    if args.folder:
        transcriber.transcribe_folder(args.folder, args.output, args.pattern)
    elif args.files:
        transcriber.transcribe_file_list(args.files, args.output)

if __name__ == "__main__":
    main()
