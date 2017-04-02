#!/usr/bin/python3
# Download new podcasts, save them to ~/Music/podcasts
import bs4
import requests
import re
import os

# ask for podcast and get the link from dictionary
websites = {'lnp': 'http://logbuch-netzpolitik.de',
            'nsfw': 'http://not-safe-for-work.de'}
selected_website = input("Please select one podcast (lnp or nsfw): ")
if selected_website.strip() in websites.keys():
    selected_website = websites[selected_website]
else:
    print("Could not resolve website. Program will quit.")
    exit()
# FOR TESTING ONLY
# print(selected_website)
# exit()
local_path = os.path.expanduser("~/Music")
link_re = re.compile('http://(.*).opus')
res = requests.get(selected_website)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")
# select opus download option of metaebene's podcasts
if selected_website == websites['lnp'] or selected_website == websites['nsfw']:
    opus = soup.select('#content .episode_downloads select option')
# insert code to find opus on other websites
dl_list = []
# go through bs4 content and look for podcast.opus and add them to a list
for i in range(0, 3):
    if 'Opus' in str(opus[i]):
            # print(str(opus[i]))
        opus_link = link_re.search(str(opus[i]))
        dl_list.append(opus_link.group())
# print(dl_list)
# ask for each podcast in list if it should be downloaded and if yes, do so.
for dl in dl_list:
    validConfirmations = ['Yes', 'yes', 'Y', 'y']
    local_filename = ''.join(local_path, dl.split('/')[-1])
    print(local_filename)
    confirmation = input("Would you like to download " + local_filename + "?")
    if confirmation.strip() in validConfirmations:
        r = requests.get(dl, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
    else:
        pass
# TODO: GUI
