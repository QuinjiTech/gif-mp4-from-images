# Image to GIF Creator

A simple Python script that creates an animated GIF from a sequence of images in a specified folder.

## Features

- Creates animated GIFs from multiple image formats (PNG, JPG, JPEG, BMP)
- Automatically handles PNG transparency
- Supports custom frame duration
- Generates timestamp-based output filenames
- Sorts images alphabetically for consistent sequence

## Requirements

- Python 3.x
- Pillow (PIL) library

Install the required package using pip:

```bash
pip install Pillow
```

## Usage

1. Place your images in the `images` folder.
2. Run the script:

```bash
python gif.py
```

The script will create a GIF named `animation-[timestamp].gif` in the same directory.

### Default Settings

- Input folder: `images/`
- Output filename: `animation-[timestamp].gif`
- Frame duration: 1000ms (1 second) per frame

### Customizing Settings

You can modify the function call in `gif.py` to change the default settings:

```python
create_gif_from_folder(
    input_folder='images',        # Change input folder path
    output_file='output.gif',     # Change output filename
    duration=1000                 # Change frame duration (milliseconds)
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

## Author's Note

This code was originally written by Atul Pathria for personal use and has been made public for the community. You are welcome to use and modify it according to your needs.

