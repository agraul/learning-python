#!/usr/bin/python3
# Downloads XKCD comics using multiple threads

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page
        print('Downloading page http://xkcd.com/{} ...' .format(urlNumber))
        res = requests.get('http://xkcd.com/{}' .format(urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.txt)

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image {}...' .format(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd',
                                          os.path.basename(comicUrl)), 'wb')
# Create and start Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(0, 1400, 100):    # loops 14 times, creates 14 threads
    downloadThread = threading.thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
