"""
Author: Atul Pathria
Company: Quinji
Created: Dec2024

A script to create MP4 videos only from a sequence of images.
"""

import cv2
import os
import time

def create_mp4_from_folder(input_folder='images', output_file='output.mp4', fps=1):
    """
    Create an MP4 video from all images in the specified folder.
    
    Args:
        input_folder (str): Path to folder containing images
        output_file (str): Name of output MP4 file
        fps (int): Frames per second for the video (default: 1 fps)
    """
    # Consider the directory as the same where the program itself is
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder_path = os.path.join(script_dir, input_folder)
    
    # Get list of image files and sort them
    image_files = [f for f in os.listdir(input_folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    image_files.sort()  # Sort files by name
    
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
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
    video = cv2.VideoWriter(output_file_path, fourcc, fps, (width, height))
    
    # Process all images
    for image_file in image_files:
        file_path = os.path.join(input_folder_path, image_file)
        try:
            frame = cv2.imread(file_path)
            if frame is not None:
                video.write(frame)
            else:
                print(f"Error loading {image_file}")
        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}")
    
    # Release the video writer
    video.release()
    print(f"MP4 video created successfully: {output_file_path}")

if __name__ == "__main__":
    # You can change these parameters as needed
    timestamp = time.strftime("%Y%m%d%H%M%S")
    create_mp4_from_folder(
        input_folder='images',  # Folder containing your images
        output_file=f'video-{timestamp}.mp4',  # Output MP4 filename with timestamp
        fps=1  # Frames per second (1 means each image shows for 1 second)
    ) 