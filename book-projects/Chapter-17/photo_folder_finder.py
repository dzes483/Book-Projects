# !/usr/bin/python3
# Goes through every folder on the user's hard drive, searching for folders in
# which more than half of the files end with either '.jpg' or '.png', and where
# the photos are larger than 500 pixels.

import os
from PIL import Image
from PIL import UnidentifiedImageError

ROOT_FOLDER = '/'
FILE_EXTS = ['jpg', 'png']

print('Scanning drive for photo folders...')
for foldername, subfolders, filenames in os.walk(ROOT_FOLDER):
    num_photo_files = 0
    num_non_photo_files = 0
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        # Ensure file extension is not .jpg or .png.
        extension = os.path.splitext(filename)[1][1:]
        if extension.lower() not in FILE_EXTS:
            num_non_photo_files += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        try:
            img = Image.open(file_path)
            img_width, img_height = img.size
        except UnidentifiedImageError or FileNotFoundError:
            pass

        # Check if width and height are larger than 500.
        if img_width > 500 and img_height > 500:
            # Image is large enough to be considered a photo.
            num_photo_files += 1
        else:
            # Image is too small to be a photo.
            num_non_photo_files += 1

    # If more than half of the files were photos:
    if num_photo_files > num_non_photo_files:
        print(f'Photo folder: {foldername}')

print('Done.')
