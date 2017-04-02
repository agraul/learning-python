#!/usr/bin/python3
import os
import re
# auto_playlist.py - generate playlist of all Music in ~/Music. by alexander graul

music_path = os.path.expanduser('~/Music/')
# Ask for name for new playlist file with fallback to "playlist.m3u"
playlist_file_name = input("Please enter a name for the playlist:\t")
if playlist_file_name == '':
    playlist_file_name = 'playlist'
playlist_file_name = music_path + playlist_file_name + '.m3u'

# create list of songs in ~/Music and subdirectories
# (only with certain fileextensions)
songs = []
audio_format_ex = re.compile(r'^(.*)?([.]mp3|[.]ogg)')
for folderName, __, fileNames in os.walk(music_path):
    for fileName in fileNames:
        match = audio_format_ex.search(folderName + '/' + fileName)
        if match is not None:
            songs.append(match.group())

# create file content for the playlist file
playlist_content = '#EXTM3U'
i = 0
while i < len(songs):
    playlist_content = playlist_content + '\n#EXTINF:' + str(i) + '\n' \
        + songs[i]
    i += 1
# write playlist content to file
with open(playlist_file_name, 'w') as pl:
    pl.write(playlist_content)
print("DONE! Playlist " + playlist_file_name + " was created successfully.")
