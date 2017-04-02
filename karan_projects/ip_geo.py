#!/usr/bin/python3

import requests
import sys

"""
Step 1) take input of ip (cli or input)
Step 2) send ip to freegeoip.net
Step 3) parse response and print
"""
try:
    ip_addr = sys.argv[1]
except IndexError:
    ip_addr = input("Please enter IPv4 adress: ")


api_url = "http://freegeoip.net/json/{}".format(ip_addr)
r = requests.get(api_url).json()
for key in r:
    if r[key]:
        print(key +": " + str(r[key]))
