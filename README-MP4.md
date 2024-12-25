# Image to MP4 Video Creator

A Python script that creates an MP4 video from a sequence of images in a specified folder.

## Features

- Creates MP4 videos from multiple image formats (PNG, JPG, JPEG, BMP)
- Customizable frame rate (FPS)
- Generates timestamp-based output filenames
- Sorts images alphabetically for consistent sequence
- Maintains original image quality

## Requirements

- Python 3.x
- OpenCV (cv2) library

Install the required package using pip:

```bash
pip install opencv-python
```

## Usage

1. Place your images in the `images` folder.
2. Run the script:

```bash
python mp4.py
```

The script will create an MP4 video named `video-[timestamp].mp4` in the same directory.

### Default Settings

- Input folder: `images/`
- Output filename: `video-[timestamp].mp4`
- Frame rate: 1 FPS (each image shows for 1 second)

### Customizing Settings

You can modify the function call in `mp4.py` to change the default settings:

```python
create_mp4_from_folder(
    input_folder='images',        # Change input folder path
    output_file='output.mp4',     # Change output filename
    fps=1                         # Change frames per second
)
```

## Supported Image Formats

- PNG
- JPG/JPEG
- BMP

## Error Handling

The script includes error handling for:
- Missing or empty folders
- Corrupted or unreadable images
- Invalid image formats
- Failed video creation

## Author's Note

This code was originally written by Atul Pathria for personal use and has been made public for the community. You are welcome to use and modify it according to your needs. 