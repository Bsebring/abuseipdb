#!/usr/bin/python

import requests
import json

url = 'https://api.abuseipdb.com/api/v2/blacklist'

headers = {
    'Key': '$YOUR_API_KEY',
    'Accept': 'text/plain'
}

response = requests.request(method='GET', url=url, headers=headers)

if response.status_code == 200:
    with open('blacklist.txt', 'w') as outFile:
        outFile.write(response.text)
    with open('blacklist.txt', 'r') as inFile:
        with open('/etc/csf/csf.deny', 'a+') as outFile:
            outFile.write(inFile.read())
else:
    print('Error contacting the server')
