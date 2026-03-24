# Whisper Transcriber - Project Documentation

## 1) Project Overview

This project provides speech-to-text transcription using OpenAI Whisper.

It includes:
- A web app built with Streamlit for uploading audio and downloading transcripts.
- A simple script for direct transcription from a local audio file.

Main folders and files:
- `transcriber-2/src/streamlit_app.py`: Main Streamlit app.
- `transcriber-2/requirements.txt`: Python dependencies.
- `transcriber-2/Dockerfile`: Container setup for deployment.
- `trans.py`: Standalone local script.

## 2) Features

- Upload audio files (`.mp3`, `.wav`, `.m4a`).
- Automatic transcription with Whisper base model.
- Download transcript as:
  - TXT
  - DOCX
  - PDF

## 3) Prerequisites

Before running locally, install:
- Python 3.9+ (recommended)
- FFmpeg (required by Whisper for audio processing)
- pip

Optional for containerized run:
- Docker Desktop

## 4) Local Setup (Windows) - Step by Step

### Step 1: Open terminal in project root

Project root should be:

`C:/Users/Solomon PC/Documents/Whisper`

### Step 2: Create virtual environment

```powershell
python -m venv .venv
```

### Step 3: Activate virtual environment

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

CMD:

```cmd
.venv\Scripts\activate.bat
```

### Step 4: Install Python dependencies

```powershell
pip install -r transcriber-2/requirements.txt
```

### Step 5: Install FFmpeg

If using winget:

```powershell
winget install Gyan.FFmpeg
```

Verify installation:

```powershell
ffmpeg -version
```

### Step 6: Run Streamlit app

```powershell
streamlit run transcriber-2/src/streamlit_app.py
```

### Step 7: Open browser

Open:

`http://localhost:8501`

### Step 8: Transcribe file

1. Upload an audio file.
2. Click Submit for Transcription.
3. Wait for processing.
4. Download as TXT, DOCX, or PDF.

SKIP THE ABOVE, SOLOMON, JUST DO THE ONE BELOW INSTEAD, YOU HEAR???
IF YOU LIKE, NO HEAR O!!!!!

## 5) Standalone Script Usage

You can also run the direct script:

```powershell
python trans.py
```

Notes:
- The script is currently hardcoded to transcribe `AUD-20250626-WA0040.m4a`.
- Ensure that file exists in the project root before running.

## 6) Docker Run - Step by Step

From project root:

### Step 1: Build image

```powershell
docker build -t whisper-transcriber ./transcriber-2
```

### Step 2: Run container

```powershell
docker run --rm -p 8501:8501 whisper-transcriber
```

### Step 3: Open browser

Open:

`http://localhost:8501`

## 7) How It Works Internally

1. The app loads Whisper base model once using Streamlit resource caching.
2. Uploaded file is written to a temporary file.
3. Whisper transcribes the temp file.
4. The temporary file is deleted.
5. Transcript is shown in UI and offered for download.

## 8) Troubleshooting

### Problem: Module not found errors

Fix:
- Activate the virtual environment.
- Reinstall dependencies:

```powershell
pip install -r transcriber-2/requirements.txt
```

### Problem: FFmpeg not found

Fix:
- Install FFmpeg and ensure it is in PATH.
- Confirm:

```powershell
ffmpeg -version
```

### Problem: App starts but no page opens

Fix:
- Open browser manually at `http://localhost:8501`.
- Check terminal for startup errors.

### Problem: First transcription is slow

Expected behavior:
- First run can be slow due to model loading/downloading.

## 9) Dependency Summary

Python packages used:
- streamlit
- whisper (from GitHub)
- ffmpeg-python
- python-docx
- torch
- reportlab

System package used:
- ffmpeg

## 10) Quick Command Reference

```powershell
# from project root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r transcriber-2/requirements.txt
streamlit run transcriber-2/src/streamlit_app.py
```
