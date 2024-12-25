"""
Author: Atul Pathria
Company: Quinji
Created: Dec2024

A script to create animated GIFs from a sequence of images.
"""

from PIL import Image
import os

def create_gif_from_folder(input_folder='images', output_file='output.gif', duration=1000):
    """
    Create an animated GIF from all images in the specified folder.
    
    Args:
        input_folder (str): Path to folder containing images
        output_file (str): Name of output GIF file
        duration (int): Duration for each frame in milliseconds (1000ms = 1sec)
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
    
    # Open all images
    images = []
    for image_file in image_files:
        file_path = os.path.join(input_folder_path, image_file)
        try:
            img = Image.open(file_path)
            # Convert to RGB if necessary (for PNG with transparency)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            images.append(img)
        except Exception as e:
            print(f"Error loading {image_file}: {str(e)}")
    
    if images:
        # Save the animated GIF
        output_file_path = os.path.join(script_dir, output_file)
        images[0].save(
            output_file_path,
            save_all=True,
            append_images=images[1:],
            duration=duration,
            loop=0
        )
        print(f"GIF created successfully: {output_file_path}")
    else:
        print("No valid images were loaded!")

if __name__ == "__main__":
    # You can change these parameters as needed
    import time
    timestamp = time.strftime("%Y%m%d%H%M%S")
    create_gif_from_folder(
        input_folder='images',  # Folder containing your images
        output_file=f'animation-{timestamp}.gif',  # Output GIF filename with timestamp
        duration=1000  # Duration for each frame in milliseconds (1000ms = 1 second)
    )
