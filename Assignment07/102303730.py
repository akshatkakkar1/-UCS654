#!/usr/bin/env python3
"""
================================================================================
YOUTUBE MASHUP PROGRAM - Assignment 07
================================================================================
Author: Akshat (102303730)
Description: 
    This program creates a mashup of YouTube videos by:
    1. Downloading N videos of a specified singer from YouTube
    2. Converting videos to audio format (MP3)
    3. Cutting first Y seconds from each audio file
    4. Merging all cut audios into a single mashup file
    5. Creating a zip file of the final output

Usage:
    python 102303730.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

Example:
    python 102303730.py "Karan Aujla" 5 30 mashup.mp3

Requirements:
    - yt-dlp: For downloading YouTube videos
    - pydub: For audio manipulation and processing
    - ffmpeg: System dependency for audio conversion
    - certifi: For SSL certificate handling
    - audioop-lts: Audio operations support for Python 3.13+

================================================================================
"""

import sys
import os
import shutil
from pathlib import Path
import yt_dlp
from pydub import AudioSegment
import ssl
import certifi
import zipfile


def download_videos(singer_name, num_videos, download_dir):
    """
    Download N videos of a singer from YouTube
    
    Args:
        singer_name: Name of the singer to search for
        num_videos: Number of videos to download
        download_dir: Directory to save downloaded videos
    
    Returns:
        List of downloaded video file paths
    """
    print(f"🔍 Searching for {num_videos} videos of '{singer_name}' on YouTube...")
    
    # Step 1.1: Configure yt-dlp options for downloading and converting
    # - format: Download best quality audio
    # - outtmpl: Set output file template with path and title
    # - ignoreerrors: Continue even if some videos fail
    # - postprocessors: Automatically convert to MP3 format after download
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best available audio quality
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Output path template
        'quiet': False,  # Show download progress
        'no_warnings': False,  # Show warnings if any
        'extract_flat': False,  # Extract full information, not just metadata
        'default_search': 'ytsearch',  # Use YouTube search
        'nocheckcertificate': False,  # Verify SSL certificates
        'ignoreerrors': True,  # Continue on download errors
        'postprocessors': [{  # Post-processing steps after download
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'mp3',  # Convert to MP3 format
            'preferredquality': '192',  # Set audio quality to 192 kbps
        }],
    }
    
    # Step 1.2: Set up SSL certificate for secure HTTPS connections
    os.environ['SSL_CERT_FILE'] = certifi.where()
    
    downloaded_files = []
    # Step 1.3: Create YouTube search query with singer name and number of videos
    # Search for extra videos to account for potential failures
    search_query = f"ytsearch{num_videos + 5}:{singer_name} songs"
    
    try:
        # Step 1.4: Initialize yt-dlp and download videos
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"📥 Downloading up to {num_videos} videos...")
            # Extract information and download videos from search results
            info = ydl.extract_info(search_query, download=True)
            
            # Step 1.5: Process downloaded files and get their paths
            # Get the downloaded files from entries
            if 'entries' in info:
                for entry in info['entries']:
                    if entry and len(downloaded_files) < num_videos:
                        # Extract video title
                        title = entry.get('title', 'Unknown')
                        # Clean the title for use in filename (remove special characters)
                        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
                        # Construct expected file path with .mp3 extension
                        file_path = os.path.join(download_dir, f"{safe_title}.mp3")
                        
                        # Check if file exists at expected path
                        if os.path.exists(file_path):
                            downloaded_files.append(file_path)
                            print(f"   ✓ Downloaded: {title[:50]}...")
                        else:
                            # Search for similar named files in download directory
                            for file in os.listdir(download_dir):
                                if file.endswith('.mp3') and safe_title[:30] in file:
                                    downloaded_files.append(os.path.join(download_dir, file))
                                    print(f"   ✓ Downloaded: {title[:50]}...")
                                    break
                    
                    # Stop if we have enough videos
                    if len(downloaded_files) >= num_videos:
                        break
        
        # Step 1.6: Fallback - if no files found through entries, scan directory for all MP3 files
        if not downloaded_files:
            downloaded_files = [
                os.path.join(download_dir, f) 
                for f in os.listdir(download_dir) 
                if f.endswith('.mp3')
            ]
        
        # Limit to requested number of files
        downloaded_files = downloaded_files[:num_videos]
        
        print(f"✅ Successfully downloaded {len(downloaded_files)} videos")
        
        # Show warning if fewer videos were downloaded than requested
        if len(downloaded_files) < num_videos:
            print(f"⚠️  Warning: Only {len(downloaded_files)} out of {num_videos} videos were downloaded")
            print(f"   This could be due to:")
            print(f"   - Limited search results on YouTube")
            print(f"   - Some videos being unavailable")
            print(f"   - Network issues")
        
        # Return only the requested number of files
        return downloaded_files
        
    except Exception as e:
        print(f"❌ Error downloading videos: {str(e)}")
        raise


def convert_and_cut_audio(audio_files, duration_seconds, output_dir):
    """
    Cut first Y seconds from each audio file
    
    Args:
        audio_files: List of audio file paths
        duration_seconds: Duration in seconds to cut from start
        output_dir: Directory to save cut audio files
    
    Returns:
        List of cut audio file paths
    """
    print(f"\n✂️  Cutting first {duration_seconds} seconds from each audio...")
    
    cut_files = []
    # Step 2.1: Process each audio file one by one
    for i, audio_file in enumerate(audio_files, 1):
        try:
            print(f"  Processing {i}/{len(audio_files)}: {os.path.basename(audio_file)}")
            
            # Step 2.2: Load the audio file using pydub
            # AudioSegment can read various audio formats (mp3, wav, etc.)
            audio = AudioSegment.from_file(audio_file)
            
            # Step 2.3: Cut first Y seconds from the audio
            # Convert seconds to milliseconds (pydub works in milliseconds)
            duration_ms = duration_seconds * 1000
            # Slice audio from start (0) to duration_ms
            cut_audio = audio[:duration_ms]
            
            # Step 2.4: Save the cut audio to output directory
            cut_filename = f"cut_{i}.mp3"  # Name files sequentially (cut_1.mp3, cut_2.mp3, etc.)
            cut_filepath = os.path.join(output_dir, cut_filename)
            # Export cut audio as MP3 format
            cut_audio.export(cut_filepath, format="mp3")
            
            # Add to list of processed files
            cut_files.append(cut_filepath)
            
        except Exception as e:
            # If any file fails, show warning but continue with other files
            print(f"  ⚠️  Warning: Could not process {audio_file}: {str(e)}")
            continue
    
    print(f"✅ Successfully cut {len(cut_files)} audio files")
    return cut_files


def merge_audio_files(audio_files, output_filename):
    """
    Merge all audio files into a single output file
    
    Args:
        audio_files: List of audio file paths to merge
        output_filename: Name of the output merged file
    """
    print(f"\n🔗 Merging {len(audio_files)} audio files...")
    
    try:
        # Step 3.1: Start with an empty audio segment
        merged_audio = AudioSegment.empty()
        
        # Step 3.2: Concatenate all audio files one by one
        for i, audio_file in enumerate(audio_files, 1):
            print(f"  Adding {i}/{len(audio_files)}: {os.path.basename(audio_file)}")
            # Load current audio file
            audio = AudioSegment.from_file(audio_file)
            # Append to merged audio (concatenate end-to-end)
            merged_audio += audio
        
        # Step 3.3: Export the merged audio to final output file
        print(f"💾 Saving merged audio to: {output_filename}")
        merged_audio.export(output_filename, format="mp3")
        
        # Step 3.4: Calculate and display file statistics
        # Get file size in megabytes
        file_size = os.path.getsize(output_filename) / (1024 * 1024)
        # Get total duration in seconds
        duration = len(merged_audio) / 1000
        
        print(f"✅ Successfully created mashup!")
        print(f"   📁 File: {output_filename}")
        print(f"   📊 Size: {file_size:.2f} MB")
        print(f"   ⏱️  Duration: {duration:.2f} seconds")
        
    except Exception as e:
        print(f"❌ Error merging audio files: {str(e)}")
        raise


def cleanup_temp_files(temp_dir):
    """Remove temporary directory and its contents"""
    try:
        # Step 4.1: Check if temporary directory exists
        if os.path.exists(temp_dir):
            # Remove entire directory tree (all subdirectories and files)
            shutil.rmtree(temp_dir)
            print(f"🧹 Cleaned up temporary files")
    except Exception as e:
        print(f"⚠️  Warning: Could not clean up temporary files: {str(e)}")


def create_zip_file(output_filename):
    """Create a zip file containing the mashup audio"""
    try:
        # Step 5.1: Generate zip filename from output filename
        # Remove .mp3 extension and add .zip
        zip_filename = output_filename.rsplit('.', 1)[0] + '.zip'
        
        print(f"\n📦 Creating zip file: {zip_filename}")
        
        # Step 5.2: Create zip file with compression
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add the mashup audio file to zip
            # First parameter: actual file path
            # Second parameter: name inside the zip file
            zipf.write(output_filename, os.path.basename(output_filename))
        
        # Step 5.3: Calculate zip file size
        zip_size = os.path.getsize(zip_filename) / (1024 * 1024)  # Convert to MB
        print(f"✅ Zip file created successfully!")
        print(f"   📁 File: {zip_filename}")
        print(f"   📊 Size: {zip_size:.2f} MB")
        
        return zip_filename
        
    except Exception as e:
        print(f"⚠️  Warning: Could not create zip file: {str(e)}")
        return None


def main():
    """Main function to handle command line arguments and orchestrate the mashup process"""
    
    # ============================================================
    # STEP 0: PARSE AND VALIDATE COMMAND LINE ARGUMENTS
    # ============================================================
    
    # Step 0.1: Check if correct number of arguments provided
    if len(sys.argv) != 5:
        print("❌ Error: Incorrect number of arguments")
        print("\n📖 Usage:")
        print("   python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        print("\n📝 Example:")
        print('   python 102303730.py "Sharry Maan" 20 20 102303730-output.mp3')
        sys.exit(1)
    
    # Step 0.2: Parse command line arguments
    singer_name = sys.argv[1]  # First argument: Singer name
    
    # Step 0.3: Validate and parse number of videos
    try:
        num_videos = int(sys.argv[2])  # Convert to integer
        if num_videos <= 0:
            print("❌ Error: Number of videos must be greater than 0")
            sys.exit(1)
    except ValueError:
        print("❌ Error: Number of videos must be a valid integer")
        sys.exit(1)
    
    # Step 0.4: Validate and parse audio duration
    try:
        audio_duration = int(sys.argv[3])  # Convert to integer
        if audio_duration <= 20:
            print("❌ Error: Audio duration must be greater than 20 seconds")
            sys.exit(1)
    except ValueError:
        print("❌ Error: Audio duration must be a valid integer")
        sys.exit(1)
    
    # Step 0.5: Get output filename
    output_filename = sys.argv[4]
    
    # ============================================================
    # DISPLAY CONFIGURATION
    # ============================================================
    print("\n" + "="*60)
    print("🎵 YOUTUBE MASHUP GENERATOR 🎵")
    print("="*60)
    print(f"👤 Singer: {singer_name}")
    print(f"📹 Videos to download: {num_videos}")
    print(f"⏱️  Audio duration per video: {audio_duration} seconds")
    print(f"📁 Output file: {output_filename}")
    print("="*60 + "\n")
    
    # ============================================================
    # SETUP TEMPORARY DIRECTORIES
    # ============================================================
    # Step 0.6: Create temporary directory structure
    temp_dir = "temp_mashup"  # Main temporary directory
    download_dir = os.path.join(temp_dir, "downloads")  # For downloaded videos
    cut_dir = os.path.join(temp_dir, "cut_audio")  # For cut audio files
    
    # Create directories if they don't exist
    os.makedirs(download_dir, exist_ok=True)
    os.makedirs(cut_dir, exist_ok=True)
    
    try:
        # ============================================================
        # STEP 1: DOWNLOAD VIDEOS FROM YOUTUBE
        # ============================================================
        downloaded_files = download_videos(singer_name, num_videos, download_dir)
        
        # Validate that videos were downloaded
        if not downloaded_files:
            print("❌ Error: No videos were downloaded")
            sys.exit(1)
        
        # ============================================================
        # STEP 2: CUT AUDIO FILES TO SPECIFIED DURATION
        # ============================================================
        cut_files = convert_and_cut_audio(downloaded_files, audio_duration, cut_dir)
        
        # Validate that audio files were processed
        if not cut_files:
            print("❌ Error: No audio files were processed")
            sys.exit(1)
        
        # ============================================================
        # STEP 3: MERGE ALL CUT AUDIO FILES INTO SINGLE FILE
        # ============================================================
        merge_audio_files(cut_files, output_filename)
        
        # ============================================================
        # STEP 4: CREATE ZIP FILE OF THE MASHUP
        # ============================================================
        zip_file = create_zip_file(output_filename)
        
        # ============================================================
        # FINAL SUCCESS MESSAGE
        # ============================================================
        print("\n" + "="*60)
        print("🎉 MASHUP COMPLETED SUCCESSFULLY! 🎉")
        print("="*60)
        if zip_file:
            print(f"📦 Your mashup is ready in: {zip_file}")
        print(f"🎵 Audio file: {output_filename}")
        print("="*60 + "\n")
        
    except KeyboardInterrupt:
        # Handle user interruption (Ctrl+C)
        print("\n\n⚠️  Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        # Handle any unexpected errors during execution
        print(f"\n❌ An error occurred: {str(e)}")
        sys.exit(1)
    finally:
        # ============================================================
        # CLEANUP: Always remove temporary files (even if error occurs)
        # ============================================================
        cleanup_temp_files(temp_dir)


if __name__ == "__main__":
    # Entry point - execute main function when script is run directly
    main()
