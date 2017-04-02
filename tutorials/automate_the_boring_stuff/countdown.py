#!/usr/bin/python3
# countdown.py - A simple countdown script.
import time
import subprocess
import sys

timeLeft = int(sys.argv[1])     # using first argument as timer duration
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

# At the send of the countdown, play a sound jfile.
subprocess.Popen(['/usr/bin/cvlc',
                  '/usr/share/sounds/alsa/test.wav'])
print('Done.')
