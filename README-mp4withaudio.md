# Image to MP4 Video Creator with Audio Support

A Python script that creates an MP4 video from a sequence of images and automatically adds audio if an MP3 file is present in the script directory.

## Features

- Creates MP4 videos from multiple image formats (PNG, JPG, JPEG, BMP)
- Automatic audio detection and integration
- Customizable frame rate (FPS)
- Generates timestamp-based output filenames
- Sorts images alphabetically for consistent sequence
- Maintains original image quality

## Requirements

- Python 3.x
- OpenCV (cv2) library
- FFmpeg
- ffmpeg-python

Install the required packages using pip:

```bash
pip install opencv-python
pip install ffmpeg-python
```

### FFmpeg Installation

- **Windows**: 
  1. Download FFmpeg from https://ffmpeg.org/download.html
  2. Add FFmpeg to your system's PATH environment variable

- **Mac**:
  ```bash
  brew install ffmpeg
  ```

- **Linux**:
  ```bash
  sudo apt-get install ffmpeg
  ```

## Usage

1. Create an `images` folder in the same directory as the script
2. Place your images in the `images` folder
3. (Optional) Place an MP3 file in the script directory for audio
4. Run the script:

```bash
python mp4.py
```

The script will:
- Create an MP4 video from your images
- Automatically detect and add any MP3 file found in the script directory
- Generate output as `video-[timestamp].mp4`

### Default Settings

- Input folder: `images/`
- Output filename: `video-[timestamp].mp4`
- Frame rate: 1 FPS (each image shows for 1 second)
- Audio: Automatically uses first MP3 file found in script directory

### Customizing Settings

You can modify the function call in `mp4.py` to change the default settings:

```python
create_mp4_from_folder(
    input_folder='images',        # Change input folder path
    output_file='output.mp4',     # Change output filename
    fps=1/3                         # Change frames per second 1/3 for 3 seconds 1
)
```

## Supported Formats

### Images
- PNG
- JPG/JPEG
- BMP

### Audio
- MP3

## Error Handling

The script includes error handling for:
- Missing or empty folders
- Corrupted or unreadable images
- Invalid image formats
- Failed video creation
- Failed audio integration
- Missing FFmpeg installation

## Troubleshooting

1. **No audio in output video**
   - Ensure MP3 file is in the same directory as the script
   - Check FFmpeg installation
   - Verify MP3 file is not corrupted

2. **Video creation fails**
   - Check image folder exists and contains supported image formats
   - Ensure sufficient disk space
   - Verify write permissions in output directory

3. **FFmpeg errors**
   - Confirm FFmpeg is properly installed
   - Check if FFmpeg is accessible from command line
   - Verify system PATH includes FFmpeg

## Author's Note

This code was originally written by Atul Pathria for personal use and has been made public for the community. You are welcome to use and modify it according to your needs.

## License

This project is open source and available under the MIT License.