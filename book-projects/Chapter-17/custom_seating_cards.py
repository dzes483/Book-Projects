# !/usr/bin/python3
# custom_seating_cards.py - Generates a seating card with a custom image
# including the guest's name.

import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

GUEST_LIST_FILE = 'GUEST_LIST_FILE'
BACKGROUND_IMG = 'BACKGROUND_IMG'
FONT_FOLDER = 'FONT_FOLDER'
FONT_FILE = 'FONT_FILE'
NEW_DIR = 'NEW_DIR'

os.makedirs(NEW_DIR, exist_ok=True)
with open(GUEST_LIST_FILE) as f:
    names = [line.rstrip() for line in f]

def place_text(img, font_size, color):
    draw = ImageDraw.Draw(img)
    card_font = ImageFont.truetype(os.path.join(FONT_FOLDER, FONT_FILE), font_size)
    w, h = draw.textsize(name, card_font)
    draw.text(((width-w)/2, (height-h)/2), name, fill=color, font=card_font)
    return img

def add_border(img, left, top, right, bottom):
    img = ImageOps.expand(placecard, border=(left, top, right, bottom))
    return img

# Loop through the guest list.
for name in names:
    # Place background image on card.
    placecard = Image.open(BACKGROUND_IMG)
    width, height = placecard.size
    # Place guest name on the card, centered.
    place_text(placecard, 80, 'black')
    # Create a border around the image.
    add_border(placecard, 5, 5, 5, 5)
    # Save the image as a new file.
    final_path = os.path.join(NEW_DIR, name)
    placecard.save(final_path + '.png')

f.close()
print('Done.')
