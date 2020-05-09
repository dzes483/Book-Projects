import requests
import os
import bs4
from bs4 import BeautifulSoup
import re
import urllib.request

# Define a search term
search_term = input('Enter a search term (this will also be the directory name): ')
os.makedirs(search_term + '_pictures', exist_ok=True)

# Check if the search term URL works
url = 'https://unsplash.com/s/photos/' + search_term
response = requests.get(url)
response.raise_for_status()

# Find all images on the page
soup = BeautifulSoup(response.content, 'html.parser')
images = soup.find_all('img')

for image in images:
    # Get the image url
    image_src = image.get('src')
    # Filter out avatar and ad images
    if image_src.startswith('https://images.unsplash.com/photo'):
        res_img = requests.get(image_src, stream=True)
        res_img.raise_for_status()

        # Write the file
        question_index = image_src.index('?')
        res_img.raw.decode_content = True
        image_file = open(os.path.join(search_term + '_pictures', os.path.basename(image_src[28:question_index] + '.jpg')), 'wb')
        for chunk in res_img.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

print('Done.')
