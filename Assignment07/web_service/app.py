"""
================================================================================
WEB SERVICE FOR YOUTUBE MASHUP - Assignment 07 (Program 2)
================================================================================
Author: Akshat (102303730)
Description: 
    FastAPI web service that creates YouTube mashups and emails them to users
    
Features:
    - Web form for user input
    - Input validation
    - Background mashup generation
    - Email delivery with zip attachment
    
================================================================================
"""

from fastapi import FastAPI, Form, Request, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import sys
import shutil
from pathlib import Path
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import uuid
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add parent directory to path to import mashup logic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import mashup functions from the main program
import yt_dlp
from pydub import AudioSegment
import certifi
import zipfile

# Initialize FastAPI app
app = FastAPI(title="YouTube Mashup Service", version="1.0")

# Setup templates directory
templates = Jinja2Templates(directory="templates")

# Create output directory for generated files
OUTPUT_DIR = "output_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# MASHUP GENERATION FUNCTIONS (from 102303730.py)
# ============================================================

def download_videos(singer_name, num_videos, download_dir):
    """Download N videos of a singer from YouTube"""
    print(f"🔍 Searching for {num_videos} videos of '{singer_name}' on YouTube...")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'quiet': False,  # Show download progress
        'no_warnings': False,  # Show warnings
        'extract_flat': False,
        'default_search': 'ytsearch',
        'nocheckcertificate': False,
        'ignoreerrors': True,  # Continue on download errors
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    os.environ['SSL_CERT_FILE'] = certifi.where()
    
    downloaded_files = []
    # Search for more videos than needed to account for failures
    search_query = f"ytsearch{num_videos + 5}:{singer_name} songs"
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"📥 Downloading up to {num_videos} videos...")
            info = ydl.extract_info(search_query, download=True)
            
            if 'entries' in info:
                for entry in info['entries']:
                    if entry and len(downloaded_files) < num_videos:
                        title = entry.get('title', 'Unknown')
                        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
                        file_path = os.path.join(download_dir, f"{safe_title}.mp3")
                        
                        if os.path.exists(file_path):
                            downloaded_files.append(file_path)
                            print(f"   ✓ Downloaded: {title[:50]}...")
                        else:
                            # Search for similar named files
                            for file in os.listdir(download_dir):
                                if file.endswith('.mp3') and safe_title[:30] in file:
                                    downloaded_files.append(os.path.join(download_dir, file))
                                    print(f"   ✓ Downloaded: {title[:50]}...")
                                    break
                    
                    # Stop if we have enough videos
                    if len(downloaded_files) >= num_videos:
                        break
        
        # Fallback: get all mp3 files in directory
        if not downloaded_files:
            downloaded_files = [
                os.path.join(download_dir, f) 
                for f in os.listdir(download_dir) 
                if f.endswith('.mp3')
            ]
        
        # Limit to requested number
        downloaded_files = downloaded_files[:num_videos]
        
        print(f"✅ Successfully downloaded {len(downloaded_files)} videos")
        
        if len(downloaded_files) < num_videos:
            print(f"⚠️  Warning: Only {len(downloaded_files)} out of {num_videos} videos were downloaded")
            print(f"   This could be due to:")
            print(f"   - Limited search results on YouTube")
            print(f"   - Some videos being unavailable")
            print(f"   - Network issues")
        
        return downloaded_files
        
    except Exception as e:
        print(f"❌ Error downloading videos: {str(e)}")
        raise


def convert_and_cut_audio(audio_files, duration_seconds, output_dir):
    """Cut first Y seconds from each audio file"""
    print(f"✂️  Cutting first {duration_seconds} seconds from each audio...")
    
    cut_files = []
    for i, audio_file in enumerate(audio_files, 1):
        try:
            audio = AudioSegment.from_file(audio_file)
            duration_ms = duration_seconds * 1000
            cut_audio = audio[:duration_ms]
            
            cut_filename = f"cut_{i}.mp3"
            cut_filepath = os.path.join(output_dir, cut_filename)
            cut_audio.export(cut_filepath, format="mp3")
            
            cut_files.append(cut_filepath)
        except Exception as e:
            print(f"⚠️  Warning: Could not process {audio_file}: {str(e)}")
            continue
    
    print(f"✅ Successfully cut {len(cut_files)} audio files")
    return cut_files


def merge_audio_files(audio_files, output_filename):
    """Merge all audio files into a single output file"""
    print(f"🔗 Merging {len(audio_files)} audio files...")
    
    try:
        merged_audio = AudioSegment.empty()
        
        for audio_file in audio_files:
            audio = AudioSegment.from_file(audio_file)
            merged_audio += audio
        
        merged_audio.export(output_filename, format="mp3")
        
        file_size = os.path.getsize(output_filename) / (1024 * 1024)
        duration = len(merged_audio) / 1000
        
        print(f"✅ Successfully created mashup!")
        print(f"   File: {output_filename}")
        print(f"   Size: {file_size:.2f} MB")
        print(f"   Duration: {duration:.2f} seconds")
        
    except Exception as e:
        print(f"❌ Error merging audio files: {str(e)}")
        raise


def create_zip_file(output_filename):
    """Create a zip file containing the mashup audio"""
    try:
        zip_filename = output_filename.rsplit('.', 1)[0] + '.zip'
        
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(output_filename, os.path.basename(output_filename))
        
        print(f"✅ Zip file created: {zip_filename}")
        return zip_filename
        
    except Exception as e:
        print(f"⚠️  Warning: Could not create zip file: {str(e)}")
        return None


# ============================================================
# EMAIL FUNCTIONALITY
# ============================================================

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def send_email_with_attachment(recipient_email, singer_name, zip_file_path):
    """
    Send email with zip file attachment
    
    Note: This is a template function. You need to configure your email settings.
    For Gmail, you need to:
    1. Enable 2-factor authentication
    2. Generate an App Password
    3. Use the App Password instead of your regular password
    """
    
    # Email configuration - Load from environment variables
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    # SMTP settings (hardcoded for Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    # Validate email configuration
    if not sender_email or not sender_password:
        print("❌ Error: Email credentials not configured in .env file")
        return False
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"Your YouTube Mashup for {singer_name} is Ready! 🎵"
        
        # Email body
        body = f"""
Hello!

Your YouTube mashup for "{singer_name}" has been successfully created!

Please find the attached zip file containing your mashup.

Details:
- Singer: {singer_name}
- Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Thank you for using our YouTube Mashup Service!

Best regards,
YouTube Mashup Team
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach zip file
        with open(zip_file_path, 'rb') as attachment:
            part = MIMEBase('application', 'zip')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(zip_file_path)}'
            )
            msg.attach(part)
        
        # Send email
        print(f"📧 Sending email to {recipient_email}...")
        
     
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Email sent successfully to {recipient_email}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        return False


# ============================================================
# BACKGROUND TASK FOR MASHUP GENERATION
# ============================================================

async def generate_mashup_task(singer_name: str, num_videos: int, duration: int, email: str):
    """
    Background task to generate mashup and send email
    This runs asynchronously so the user doesn't have to wait
    """
    
    # Generate unique ID for this request
    request_id = str(uuid.uuid4())[:8]
    
    # Create temporary directories
    temp_dir = os.path.join(OUTPUT_DIR, f"temp_{request_id}")
    download_dir = os.path.join(temp_dir, "downloads")
    cut_dir = os.path.join(temp_dir, "cut_audio")
    
    os.makedirs(download_dir, exist_ok=True)
    os.makedirs(cut_dir, exist_ok=True)
    
    # Initialize file paths
    output_filename = None
    zip_file = None
    
    try:
        print(f"\n{'='*60}")
        print(f"🎵 Starting mashup generation for {singer_name}")
        print(f"Request ID: {request_id}")
        print(f"{'='*60}\n")
        
        # Step 1: Download videos
        downloaded_files = download_videos(singer_name, num_videos, download_dir)
        
        if not downloaded_files:
            raise Exception("No videos were downloaded")
        
        # Step 2: Cut audio files
        cut_files = convert_and_cut_audio(downloaded_files, duration, cut_dir)
        
        if not cut_files:
            raise Exception("No audio files were processed")
        
        # Step 3: Merge audio files
        output_filename = os.path.join(OUTPUT_DIR, f"mashup_{request_id}.mp3")
        merge_audio_files(cut_files, output_filename)
        
        # Step 4: Create zip file
        zip_file = create_zip_file(output_filename)
        
        if not zip_file:
            raise Exception("Failed to create zip file")
        
        # Step 5: Send email
        email_sent = send_email_with_attachment(email, singer_name, zip_file)
        
        if email_sent:
            print(f"\n{'='*60}")
            print(f"🎉 Mashup completed and email sent!")
            print(f"{'='*60}\n")
            
            # Step 6: Clean up output files after successful email delivery
            try:
                if os.path.exists(output_filename):
                    os.remove(output_filename)
                    print(f"🗑️  Deleted output file: {output_filename}")
                
                if os.path.exists(zip_file):
                    os.remove(zip_file)
                    print(f"🗑️  Deleted zip file: {zip_file}")
            except Exception as cleanup_error:
                print(f"⚠️  Warning: Could not delete output files: {str(cleanup_error)}")
        else:
            print(f"\n⚠️  Mashup created but email sending failed")
            print(f"   Files kept for debugging:")
            print(f"   - {output_filename}")
            print(f"   - {zip_file}")
        
        # Cleanup temporary files
        shutil.rmtree(temp_dir)
        print(f"🧹 Cleaned up temporary files")
        
    except Exception as e:
        print(f"\n❌ Error in mashup generation: {str(e)}\n")
        
        # Cleanup temporary files
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        
        # Cleanup output files on error
        try:
            if output_filename and os.path.exists(output_filename):
                os.remove(output_filename)
                print(f"🗑️  Deleted incomplete output file")
            
            if zip_file and os.path.exists(zip_file):
                os.remove(zip_file)
                print(f"🗑️  Deleted incomplete zip file")
        except Exception as cleanup_error:
            print(f"⚠️  Warning: Could not delete incomplete files: {str(cleanup_error)}")


# ============================================================
# API ENDPOINTS
# ============================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main page with the form"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate-mashup")
async def generate_mashup(
    background_tasks: BackgroundTasks,
    singer_name: str = Form(...),
    num_videos: int = Form(...),
    duration: int = Form(...),
    email: str = Form(...)
):
    """
    Handle mashup generation request
    Validates inputs and starts background task
    """
    
    # Validation
    errors = []
    
    # Validate singer name
    if not singer_name or len(singer_name.strip()) == 0:
        errors.append("Singer name is required")
    
    # Validate number of videos
    try:
        if num_videos < 10:
            errors.append("Number of videos must be greater than 10")
    except (TypeError, ValueError):
        errors.append("Number of videos must be a valid integer")
    
    # Validate duration
    try:
        if duration < 21:
            errors.append("Duration must be greater than 20 seconds")
    except (TypeError, ValueError):
        errors.append("Duration must be a valid integer")
    
    # Validate email
    if not validate_email(email):
        errors.append("Invalid email format")
    
    # If there are errors, return them
    if errors:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "errors": errors
            }
        )
    
    # All validations passed - start background task
    background_tasks.add_task(
        generate_mashup_task,
        singer_name,
        num_videos,
        duration,
        email
    )
    
    # Return immediate response
    return JSONResponse(
        content={
            "success": True,
            "message": f"Your mashup for '{singer_name}' is being generated! You will receive an email at {email} once it's ready.",
            "estimated_time": "5-10 minutes depending on the number of videos"
        }
    )


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "YouTube Mashup Generator"}


# ============================================================
# RUN THE APPLICATION
# ============================================================

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("🎵 YouTube Mashup Web Service")
    print("="*60)
    print("Starting server on http://localhost:8000")
    print("Press Ctrl+C to stop")
    print("="*60 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
