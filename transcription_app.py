#!/usr/bin/env python3
"""
Speech-to-Text Transcription Tool
A GUI application for transcribing MP3 and WAV audio files using OpenAI Whisper
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import whisper
import threading
import os
import sys
from pathlib import Path
import time

class TranscriptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech-to-Text Transcription Tool")
        self.root.geometry("800x600")
        
        # Initialize Whisper model
        self.model = None
        self.model_size = tk.StringVar(value="base")
        
        # Create GUI elements
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Audio Transcription Tool", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Model selection
        ttk.Label(main_frame, text="Whisper Model:").grid(row=1, column=0, sticky=tk.W, pady=5)
        model_combo = ttk.Combobox(main_frame, textvariable=self.model_size, 
                                  values=["tiny", "base", "small", "medium", "large"], 
                                  state="readonly", width=15)
        model_combo.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Load model button
        load_model_btn = ttk.Button(main_frame, text="Load Model", 
                                   command=self.load_model)
        load_model_btn.grid(row=1, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # File selection
        ttk.Label(main_frame, text="Audio File:").grid(row=2, column=0, sticky=tk.W, pady=5)
        
        file_frame = ttk.Frame(main_frame)
        file_frame.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        file_frame.columnconfigure(0, weight=1)
        
        self.file_path_var = tk.StringVar()
        file_entry = ttk.Entry(file_frame, textvariable=self.file_path_var, state="readonly")
        file_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        browse_btn = ttk.Button(file_frame, text="Browse", command=self.browse_file)
        browse_btn.grid(row=0, column=1)
        
        # Transcribe button
        self.transcribe_btn = ttk.Button(main_frame, text="Transcribe Audio", 
                                        command=self.transcribe_audio, state="disabled")
        self.transcribe_btn.grid(row=3, column=0, columnspan=3, pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status label
        self.status_var = tk.StringVar(value="Select a model and audio file to begin")
        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=5, column=0, columnspan=3, pady=5)
        
        # Transcription output
        ttk.Label(main_frame, text="Transcription:").grid(row=6, column=0, sticky=(tk.W, tk.N), pady=(20, 5))
        
        self.transcript_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, 
                                                        height=15, width=80)
        self.transcript_text.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), 
                                 pady=5)
        main_frame.rowconfigure(7, weight=1)
        
        # Save buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=8, column=0, columnspan=3, pady=10)
        
        save_btn = ttk.Button(button_frame, text="Save Transcript", 
                             command=self.save_transcript)
        save_btn.pack(side=tk.LEFT, padx=5)
        
        copy_btn = ttk.Button(button_frame, text="Copy to Clipboard", 
                             command=self.copy_transcript)
        copy_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = ttk.Button(button_frame, text="Clear", 
                              command=self.clear_transcript)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
    def load_model(self):
        """Load the selected Whisper model"""
        def load_in_thread():
            try:
                self.status_var.set(f"Loading {self.model_size.get()} model...")
                self.progress.start()
                self.model = whisper.load_model(self.model_size.get())
                self.progress.stop()
                self.status_var.set(f"Model '{self.model_size.get()}' loaded successfully")
                self.check_ready_state()
            except Exception as e:
                self.progress.stop()
                self.status_var.set("Error loading model")
                messagebox.showerror("Error", f"Failed to load model: {str(e)}")
        
        # Run in separate thread to prevent UI freezing
        thread = threading.Thread(target=load_in_thread)
        thread.daemon = True
        thread.start()
    
    def browse_file(self):
        """Browse for audio file"""
        filetypes = (
            ('Audio files', '*.mp3 *.wav *.m4a *.flac *.ogg'),
            ('MP3 files', '*.mp3'),
            ('WAV files', '*.wav'),
            ('All files', '*.*')
        )
        
        filename = filedialog.askopenfilename(
            title='Select audio file',
            initialdir=os.getcwd(),
            filetypes=filetypes
        )
        
        if filename:
            self.file_path_var.set(filename)
            self.check_ready_state()
    
    def check_ready_state(self):
        """Check if ready to transcribe"""
        if self.model is not None and self.file_path_var.get():
            self.transcribe_btn.config(state="normal")
            self.status_var.set("Ready to transcribe")
        else:
            self.transcribe_btn.config(state="disabled")
    
    def transcribe_audio(self):
        """Transcribe the selected audio file"""
        def transcribe_in_thread():
            try:
                file_path = self.file_path_var.get()
                if not os.path.exists(file_path):
                    messagebox.showerror("Error", "Selected file does not exist")
                    return
                
                self.status_var.set("Transcribing audio...")
                self.progress.start()
                self.transcribe_btn.config(state="disabled")
                
                # Clear previous transcript
                self.transcript_text.delete(1.0, tk.END)
                
                # Transcribe
                result = self.model.transcribe(file_path)
                transcript = result["text"].strip()
                
                # Display transcript
                self.transcript_text.insert(tk.END, transcript)
                
                self.progress.stop()
                self.status_var.set(f"Transcription completed for: {os.path.basename(file_path)}")
                self.transcribe_btn.config(state="normal")
                
            except Exception as e:
                self.progress.stop()
                self.transcribe_btn.config(state="normal")
                self.status_var.set("Error during transcription")
                messagebox.showerror("Error", f"Failed to transcribe audio: {str(e)}")
        
        # Run in separate thread
        thread = threading.Thread(target=transcribe_in_thread)
        thread.daemon = True
        thread.start()
    
    def save_transcript(self):
        """Save transcript to file"""
        transcript = self.transcript_text.get(1.0, tk.END).strip()
        if not transcript:
            messagebox.showwarning("Warning", "No transcript to save")
            return
        
        filename = filedialog.asksaveasfilename(
            title='Save transcript',
            defaultextension='.txt',
            filetypes=[('Text files', '*.txt'), ('All files', '*.*')]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(transcript)
                messagebox.showinfo("Success", f"Transcript saved to: {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save transcript: {str(e)}")
    
    def copy_transcript(self):
        """Copy transcript to clipboard"""
        transcript = self.transcript_text.get(1.0, tk.END).strip()
        if not transcript:
            messagebox.showwarning("Warning", "No transcript to copy")
            return
        
        self.root.clipboard_clear()
        self.root.clipboard_append(transcript)
        messagebox.showinfo("Success", "Transcript copied to clipboard")
    
    def clear_transcript(self):
        """Clear the transcript text"""
        self.transcript_text.delete(1.0, tk.END)
        self.status_var.set("Transcript cleared")

def main():
    """Main function"""
    root = tk.Tk()
    app = TranscriptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
