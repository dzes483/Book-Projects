#! python3
# link_verification.py - This program will download every linked page on the
# given URL. Pages with a 404 "Not Found" error are flagged as broken links.

import requests
import bs4
from bs4 import BeautifulSoup

# Define an URL *change to input later
url = input('Enter a URL: ')

# Download the initial page and check that it exists
response = requests.get(url)
response.raise_for_status()

# Find the anchor tags
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a')

# Find all of the links in the anchor tags
for link in links:
    link_url = link.get('href')
    if link_url != None and link_url.startswith('http'):
        link_response = requests.get(link_url)
        # If there is an error, print 'Broken link'
        if link_response.status_code == 404:
            print(f'Broken link: {link_url}')
        else:
            print(f'Valid link: {link_url}')

print('Done.')
