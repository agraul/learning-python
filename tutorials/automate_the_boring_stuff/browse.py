#!/usr/bin/env python3
# browse_suse.py - open openSUSE related websites in a a browser.
import webbrowser
website_list = ['news.opensuse.org', 'opensuse-forum.de', 'forums.opensuse.org',
                'lwn.net', 'opensuse.reddit.com']
webbrowser.open_new('https://software.opensuse.org/find')
for website in website_list:
    webbrowser.open('https://' + website)
