#!/usr/bin/python3
# scheduled_comic_downloader.py - Automatically downloads one comic per day
# from a selection of comic websites, if there is a new comic available for
# that day.

import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup
import datetime
import os

comic_urls = ['http://www.lefthandedtoons.com/', 'http://www.happletea.com/',
              'https://www.exocomics.com/']


def find_and_convert_dt(name, key, value, date_format, time):
    # Extract the date and strip leading and trailing whitespace.
    element = soup.find(name, attrs={key: value})
    post_date = element.text.strip()

    # Change the post date into a datetime object, then back to a
    # string, to compensate for days on the website that only have one
    # digit instead of two (i.e. May 6, not May 06).
    if time == False:
        # If the datetime object does not contain a time:
        post_date = datetime.datetime.strptime(post_date, date_format)
        post_date = post_date.strftime(date_format)
        return post_date
    else:
        post_date = datetime.datetime.strptime(post_date[:-11], date_format)
        post_date = post_date.strftime(date_format)
        return post_date


def dwnld_comic_img(img_name, site_name):
    for image in images:
        # Get the image's URL.
        image_src = image.get('src')
        file_ext = image_src[-1:-5]
        if image_src.startswith(img_name):
            res_img = requests.get(image_src, stream=True)
            res_img.raise_for_status()
            res_img.raw.decode_content = True
            image_file = open(os.path.join(desktop_path, site_name + '-' + \
                                           file_name_today + file_ext), 'wb')
            for chunk in res_img.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

for url in comic_urls:
    response = requests.get(url)
    try:
        # Raise for status, making sure it is still a valid link.
        response.raise_for_status()
    except HTTPError:
        print('Unable to connect to website.')
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        today = datetime.datetime.now()
        file_name_today = datetime.datetime.today().strftime('%Y-%m-%d')
        desktop_path = 'desktop_path'
        if url.startswith('http://www.lefthandedtoons.com/'):

            # Remove the Header 1 tag, since there is extra unneeded text.
            h1_tag = soup.h1
            h1_tag.decompose()

            # Convert the comic date to a string
            post_date = find_and_convert_dt('div', 'class', 'comictitlearea', \
                                            '%B %d, %Y', False)
            # Convert today's date into the same format
            today = today.strftime('%B %d, %Y') # format: January 1, 2000

            # If there is a new image for today, download and save it.
            if post_date == today:
                print('Downloading comic...')
                images = soup.find_all('img')
                dwnld_comic_img('http://www.lefthandedtoons.com/toons/', \
                                'lefthandedtoons')

        elif url.endswith('http://www.happletea.com/'):
            post_date = find_and_convert_dt('span', 'class', 'post-date', \
                                            '%B %d, %Y', False)
            today = today.strftime('%B %d, %Y') # format: January 1, 2000
            if post_date == today:
                images = soup.find_all('img')
                print('Downloading comic...')
                dwnld_comic_img('http://www.happletea.com/wp-content/uploads/',\
                                'happletea')

        elif url.endswith('https://www.exocomics.com/'):
            post_date = find_and_convert_dt('p', 'class', 'date', "%d %B '%y",\
                                            False)
            today = today.strftime("%d %B '%y") # format: 1 January '00
            if post_date == today:
                images = soup.find_all('img')
                print('Downloading comic...')
                dwnld_comic_img('https://www.exocomics.com/wp-content/uploads/'\
                                , 'exocomics')

print('Done.')
