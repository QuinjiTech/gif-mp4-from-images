"""
Author: Atul Pathria
Company: Quinji
Created: Dec2024

A script to create MP4 videos from a sequence of images with automatic audio support.
"""

import cv2
import os
import time
import subprocess
import ffmpeg

def find_audio_file(folder_path):
    """Find the first audio file (mp3) in the specified folder."""
    for file in os.listdir(folder_path):
        if file.lower().endswith('.mp3'):
            return os.path.join(folder_path, file)
    return None

def create_mp4_from_folder(input_folder='images', output_file='output.mp4', fps=1):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder_path = os.path.join(script_dir, input_folder)
    
    # Find audio file if exists
    audio_file = find_audio_file(script_dir)
    if audio_file:
        print(f"Found audio file: {os.path.basename(audio_file)}")
    
    # Get list of image files and sort them
    image_files = [f for f in os.listdir(input_folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    image_files.sort()
    
    if not image_files:
        print("No image files found in the specified folder!")
        return
    
    # Read the first image to get dimensions
    first_image_path = os.path.join(input_folder_path, image_files[0])
    frame = cv2.imread(first_image_path)
    if frame is None:
        print(f"Error loading first image: {image_files[0]}")
        return
    
    height, width, layers = frame.shape
    
    # Initialize video writer
    output_file_path = os.path.join(script_dir, output_file)
    temp_video_path = output_file_path.replace('.mp4', '_temp.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))
    
    # Process all images
    frame_count = 0
    for image_file in image_files:
        file_path = os.path.join(input_folder_path, image_file)
        try:
            frame = cv2.imread(file_path)
            if frame is not None:
                video.write(frame)
                frame_count += 1
            else:
                print(f"Error loading {image_file}")
        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}")
    
    video.release()
    
    if audio_file:
        try:
            print("Adding audio to video...")
            # Use ffmpeg to combine video and audio
            cmd = [
                'ffmpeg', '-y',
                '-i', temp_video_path,
                '-i', audio_file,
                '-c:v', 'copy',
                '-c:a', 'aac',
                '-shortest',
                output_file_path
            ]
            subprocess.run(cmd, check=True)
            os.remove(temp_video_path)  # Clean up temp file
            print("Audio added successfully!")
        except Exception as e:
            print(f"Error adding audio: {str(e)}")
            # If audio fails, just use the video without audio
            os.rename(temp_video_path, output_file_path)
    else:
        os.rename(temp_video_path, output_file_path)
        print("No audio file found in the script directory. Creating video without audio.")
    
    print(f"MP4 video created successfully: {output_file_path}")

if __name__ == "__main__":
    timestamp = time.strftime("%Y%m%d%H%M%S")
    create_mp4_from_folder(
        input_folder='images',
        output_file=f'video-{timestamp}.mp4',
        fps=1/2
    ) 