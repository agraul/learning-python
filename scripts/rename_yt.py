#!/usr/bin/python3
import re
import os
import shutil

# rename_yt.py - strip video ID from youtube downloads

# Use current directory
cwd = os.getcwd()
pattern = re.compile(r"^(.*?)(-(\S){11})([.]mp4$|[.]webm$|[.]mkv$)")
renamed_files = 'Renamed :'
for file in os.listdir(cwd):
    mo = pattern.search(file)
    if mo is None:
        continue
    video_name = mo.group(1)
    video_id = mo.group(2)
    video_extension = mo.group(4)
    renamed_files = renamed_files + '\n' + video_name + video_extension
    old_name = os.path.join(cwd, file)
    new_name = os.path.join(cwd, video_name + video_extension)
    shutil.move(old_name, new_name)

print(renamed_files)
