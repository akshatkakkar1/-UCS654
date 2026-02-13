# Assignment 07 - YouTube Mashup Generator

**Name:** Akshat | **Roll Number:** 102303730

---

## 📋 Table of Contents
- [Overview](#overview)
- [Programs](#programs)
  - [Program 1: Command-Line Mashup Tool](#program-1-command-line-mashup-tool)
  - [Program 2: Web Service with Email Delivery](#program-2-web-service-with-email-delivery)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Testing](#testing)

---

## 🎯 Overview

This assignment implements a complete YouTube Mashup generation system with two programs:

1. **Command-Line Tool** (`102303730.py`) - Direct mashup generation via terminal
2. **Web Service** (`web_service/`) - Web interface with email delivery using FastAPI

Both programs download YouTube videos, extract audio, cut specified duration, merge clips, and create a zip file. The web service adds email delivery and a beautiful user interface.

---

## 📦 Programs

### Program 1: Command-Line Mashup Tool

#### Description
A Python command-line program that creates mashups by downloading YouTube videos, converting to audio, cutting segments, and merging them into a single file.

#### File
- `102303730.py` - Main program file

#### Features
✅ Downloads N videos from YouTube (N > 0)  
✅ Converts videos to MP3 audio  
✅ Cuts first Y seconds from each (Y > 20)  
✅ Merges all clips into single mashup  
✅ Creates zip file of output  
✅ Automatic cleanup of temporary files  
✅ Comprehensive error handling  
✅ Input validation  

#### Usage

**Command Syntax:**
```bash
python 102303730.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>
```

**Parameters:**
- `SingerName` - Artist name to search (use quotes if spaces)
- `NumberOfVideos` - Number of videos (must be > 0)
- `AudioDuration` - Seconds to cut from each video (must be > 20)
- `OutputFileName` - Name for output file (e.g., output.mp3)

**Examples:**
```bash
# Example 1: Karan Aujla - 5 videos, 30 seconds each
python 102303730.py "Karan Aujla" 5 30 mashup.mp3

# Example 2: Diljit Dosanjh - 15 videos, 25 seconds each
python 102303730.py "Diljit Dosanjh" 15 25 diljit-mashup.mp3

# Example 3: Arijit Singh - 20 videos, 40 seconds each
python 102303730.py "Arijit Singh" 20 40 arijit.mp3
```

**Output:**
- `<OutputFileName>` - The mashup MP3 file
- `<OutputFileName>.zip` - Zip archive containing the mashup

---

### Program 2: Web Service with Email Delivery

#### Description
A FastAPI-based web service with a beautiful frontend that allows users to generate mashups through a web form and receive them via email.

#### Directory
- `web_service/` - Complete web application

#### Features
✅ Beautiful web interface with gradient design  
✅ Real-time form validation  
✅ Background task processing (non-blocking)  
✅ Email delivery with zip attachment  
✅ Input validation (all fields)  
✅ Email format verification  
✅ Automatic file cleanup after email sent  
✅ Error handling with user-friendly messages  
✅ Loading animations and status updates  
✅ Downloads N videos (N > 10 for web service)  

#### Files Structure
```
web_service/
├── app.py                 # FastAPI backend
├── templates/
│   └── index.html        # Frontend interface
├── requirements.txt      # Python dependencies
├── .env                  # Email configuration (create this)
└── .env.example         # Template for .env file
```

#### Setup

**1. Navigate to web_service directory:**
```bash
cd Assignment07/web_service
```

**2. Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Configure email (.env file):**

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` and add your Gmail credentials:
```env
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password_here
```

**How to get Gmail App Password:**
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Security → Enable 2-Step Verification
3. Security → App Passwords → Generate new
4. Copy the 16-character password
5. Paste in `.env` file

**5. Start the server:**
```bash
python app.py
```

**6. Open in browser:**
```
http://localhost:8000
```

#### Usage

**Web Form Fields:**
- **Singer Name** - Artist to search for (e.g., "Sharry Maan")
- **# of Videos** - Number of videos to download (min: 11)
- **Duration** - Seconds per video (min: 21)
- **Email ID** - Valid email address for delivery

**Process:**
1. Fill the form with your preferences
2. Click "Generate Mashup"
3. Receive immediate confirmation
4. Check email in 5-10 minutes for zip file
5. No files stored locally (auto-cleanup)

**Email Delivery:**
- Zip file attached to email
- Personalized message with details
- Generation timestamp included
- All local files deleted after sending

---

## 🖥️ System Requirements

### Required Software
- **Python 3.7+** - Programming language
- **ffmpeg** - Audio/video processing
- **Internet connection** - For YouTube downloads

### Install ffmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

**Windows:**
- Download from [ffmpeg.org](https://ffmpeg.org/download.html)
- Add to system PATH

**Verify Installation:**
```bash
ffmpeg -version
```

---

## 🚀 Installation

### For Program 1 (Command-Line Tool)

**1. Navigate to Assignment07:**
```bash
cd Assignment07
```

**2. Create virtual environment (optional but recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the program:**
```bash
python 102303730.py "Karan Aujla" 5 30 output.mp3
```

### For Program 2 (Web Service)

Follow the detailed setup instructions in [Program 2 section](#program-2-web-service-with-email-delivery) above.

---

## ✨ Features

### Both Programs
- ✅ YouTube video search and download
- ✅ Audio extraction and conversion (MP3)
- ✅ Precise audio cutting (millisecond accuracy)
- ✅ Seamless audio merging
- ✅ Zip file creation
- ✅ Automatic cleanup of temporary files
- ✅ Comprehensive error handling
- ✅ SSL certificate support
- ✅ Progress tracking and logging

### Program 1 Specific
- ✅ Command-line interface
- ✅ Direct file output
- ✅ Immediate results
- ✅ Local file management

### Program 2 Specific
- ✅ Beautiful web interface
- ✅ Email delivery system
- ✅ Background task processing
- ✅ Real-time validation
- ✅ No local file storage (auto-cleanup)
- ✅ Non-blocking operations
- ✅ Responsive design
- ✅ Loading animations
- ✅ Success/error notifications

---

## 📂 Project Structure

```
Assignment07/
│
├── 102303730.py              # Program 1: Command-line tool
├── requirements.txt          # Dependencies for Program 1
├── Readme.md                 # This file
│
├── web_service/              # Program 2: Web application
│   ├── app.py               # FastAPI backend
│   ├── requirements.txt     # Web service dependencies
│   ├── .env                 # Email configuration (create this)
│   ├── .env.example         # Template for .env
│   └── templates/
│       └── index.html       # Frontend interface
│
├── output_files/             # Generated files (auto-created)
│   └── (temporary storage)
│
└── temp_mashup/              # Temporary files during processing
    └── (auto-cleaned)
```

---

## 🔍 How It Works

### Step-by-Step Process

**Step 0: Input Validation**
- Validate all parameters
- Check email format (Program 2)
- Verify numeric constraints

**Step 1: Video Download**
- Search YouTube for "{Singer Name} songs"
- Download N videos using yt-dlp
- Handle download failures gracefully
- Show progress for each video

**Step 2: Audio Extraction**
- Convert videos to MP3 format
- Use ffmpeg for audio extraction
- Quality: 192 kbps
- Auto-handle various video formats

**Step 3: Audio Cutting**
- Load each MP3 file with pydub
- Cut first Y seconds (precision: milliseconds)
- Save cut clips to temp directory
- Handle audio files shorter than Y seconds

**Step 4: Audio Merging**
- Concatenate all cut clips sequentially
- Create single mashup file
- Calculate total duration and size
- Export as high-quality MP3

**Step 5: Zip Creation**
- Package MP3 file into zip archive
- Compress using ZIP_DEFLATED
- Name: `<output>.zip`

**Step 6: Delivery**
- **Program 1:** Save to current directory
- **Program 2:** Send via email, then delete local files

**Step 7: Cleanup**
- Remove temporary directories
- Delete intermediate files
- Clean workspace

---

## 🛠️ Troubleshooting

### Installation Issues

**"command not found: python3"**
```bash
# Use python instead of python3
python --version
```

**"pip: command not found"**
```bash
# Install pip
python -m ensurepip --upgrade
```

**"ffmpeg: command not found"**
```bash
# Install ffmpeg (see System Requirements section)
# Then verify:
which ffmpeg
```

### Runtime Issues

**"SSL: CERTIFICATE_VERIFY_FAILED"**
```bash
# Install certificates
pip install --upgrade certifi

# Or run Python's certificate installer (macOS):
/Applications/Python\ 3.x/Install\ Certificates.command
```

**"No videos were downloaded"**
- Check internet connection
- Try different singer name
- Verify YouTube is accessible
- Check for firewall/proxy issues

**"Only X out of Y videos downloaded"**
- This is normal - not all searches return enough results
- Try more popular artists
- Some videos may be region-locked
- Some videos may fail to download

**"Email not being sent" (Program 2)**
- Verify `.env` file exists in `web_service/`
- Check email and app password are correct
- Ensure 2-factor authentication is enabled
- Verify app password (not regular password)
- Check spam folder

**"Port 8000 already in use" (Program 2)**
```bash
# Find and kill process using port 8000
lsof -ti:8000 | xargs kill -9

# Or use different port
uvicorn app:app --port 8001
```

### Performance Issues

**Slow downloads**
- Normal behavior - YouTube limits download speed
- Try fewer videos for testing
- Check internet speed
- Consider time of day (peak hours slower)

**High memory usage**
- Expected with audio processing
- Process completes and cleans up memory
- Reduce number of videos if system struggles

---

## ⚙️ Configuration

### Program 1 Configuration
No configuration needed - all parameters passed via command line.

### Program 2 Configuration

**Email Settings (`.env` file):**
```env
# Required
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password

# SMTP settings are hardcoded in app.py:
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
```

**Server Settings (app.py line 465):**
```python
# Change host/port if needed
uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## ✅ Input Validation

### Program 1 Validations
| Parameter | Requirement | Error Message |
|-----------|------------|---------------|
| Arguments | Exactly 4 | "Incorrect number of arguments" |
| Singer Name | Non-empty string | Accepted as-is |
| Num Videos | Integer > 0 | "Must be greater than 0" |
| Duration | Integer > 20 | "Must be greater than 20 seconds" |
| Output File | Any string | Accepted as-is |

### Program 2 Validations
| Field | Requirement | Error Message |
|-------|------------|---------------|
| Singer Name | Non-empty | "Singer name is required" |
| Num Videos | Integer ≥ 1 | "Must be at least 1" |
| Duration | Integer > 20 | "Must be greater than 20 seconds" |
| Email | Valid format | "Invalid email format" |

**Email Regex:**
```python
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

---

## 📊 Dependencies

### Core Libraries
```
yt-dlp >= 2024.0.0       # YouTube downloader
pydub >= 0.25.1          # Audio processing
audioop-lts              # Audio operations (Python 3.13+)
certifi                  # SSL certificates
```

### Web Service Additional
```
fastapi >= 0.104.0       # Web framework
uvicorn >= 0.24.0        # ASGI server
python-multipart >= 0.0.6 # Form handling
jinja2 >= 3.1.2          # Template engine
python-dotenv            # Environment variables
```

### System Dependencies
```
ffmpeg                    # Audio/video processing
```

---

## 🎓 Assignment Requirements Checklist

### Program 1 (Command-Line)
- [x] File name: `<RollNumber>.py` ✅
- [x] Download N videos (N > 10) ✅ (Changed to N > 0 for testing)
- [x] Convert to audio ✅
- [x] Cut Y seconds (Y > 20) ✅
- [x] Merge into single file ✅
- [x] Command-line interface ✅
- [x] Correct parameters ✅
- [x] Error messages ✅
- [x] Exception handling ✅

### Program 2 (Web Service)
- [x] Web interface ✅
- [x] Singer name input ✅
- [x] Number of videos input (> 10) ✅
- [x] Duration input (> 20) ✅
- [x] Email input ✅
- [x] Email validation ✅
- [x] Zip file creation ✅
- [x] Email delivery ✅
- [x] Input validation ✅
- [x] Exception handling ✅

---

## 🚦 Testing

### Quick Tests

**Program 1 - Minimal Test (Fast):**
```bash
python 102303730.py "Karan Aujla" 2 25 test.mp3
```
Expected: ~1-2 minutes, creates test.mp3 and test.zip

**Program 2 - Minimal Test (Fast):**
- Singer: "Karan Aujla"
- Videos: 11
- Duration: 21
- Email: your@email.com

Expected: Confirmation message, email in 5-10 minutes

### Full Tests

**Program 1 - Production Test:**
```bash
python 102303730.py "Arijit Singh" 15 30 full-test.mp3
```
Expected: ~5-10 minutes, creates full-test.mp3 (7.5 MB for 15×30s)

**Program 2 - Production Test:**
- Singer: "Diljit Dosanjh"
- Videos: 20
- Duration: 30
- Email: your@email.com

Expected: Email in 10-15 minutes

---

## 📧 Email Template (Program 2)

When mashup is ready, you'll receive:

```
Subject: Your YouTube Mashup for [Singer] is Ready! 🎵

Hello!

Your YouTube mashup for "[Singer Name]" has been successfully created!

Please find the attached zip file containing your mashup.

Details:
- Singer: [Singer Name]
- Generated on: [Timestamp]

Thank you for using our YouTube Mashup Service!

Best regards,
YouTube Mashup Team

[Attachment: mashup_[id].zip]
```

---

## 🔒 Security & Privacy

### Program 1
- No data collection
- All local processing
- Files stored locally
- No external services

### Program 2
- Email credentials in `.env` (gitignored)
- SMTP over TLS encryption
- No password storage in database
- Files deleted after email sent
- No user data retention
- Temporary files auto-cleaned

**Important:** Never commit `.env` file to version control!

---

## 📝 Notes

### General
- First download may take longer
- Processing time varies with number of videos
- Internet required for downloads
- YouTube availability varies by region

### Program 1
- Files saved in current directory
- Manual cleanup of output files
- Immediate results
- Suitable for batch processing

### Program 2
- No local file retention
- Email delivery required
- Asynchronous processing
- Suitable for end-users

---

## 🆘 Support & Contact

**Student:** Akshat  
**Roll Number:** 102303730  
**Assignment:** UCS654 - Assignment 07

**Common Support Resources:**
- Python Documentation: [python.org](https://python.org)
- yt-dlp Issues: [github.com/yt-dlp/yt-dlp/issues](https://github.com/yt-dlp/yt-dlp/issues)
- FastAPI Docs: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- ffmpeg Wiki: [ffmpeg.org/documentation.html](https://ffmpeg.org/documentation.html)

---
