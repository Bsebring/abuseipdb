#!/usr/bin/python

import requests
import json

url = 'https://api.abuseipdb.com/api/v2/blacklist'

headers = {
    'Key': '$YOUR_API_KEY',
    'Accept': 'text/plain'
}

response = requests.request(method='GET', url=url, headers=headers)
decodedResponse = json.loads(response.text)

if response.status_code == 200:
    with open('blacklist.txt', 'w') as outFile:
        outFile.write(response.text)
    with open('blacklist.txt', 'r') as inFile, \
         open('/etc/csf/csf.deny', 'a+') as outFile:
            outFile.write(inFile.read())
elif response.status_code == 429:
    print (json.dumps(decodedResponse['errors'][0], sort_keys=True, indent=4))
elif response.status_code == 422:
    print (json.dumps(decodedResponse['errors'], sort_keys=True, indent=4))
elif response.status_code == 302:
    print('Unsecure protocol requested. Redirected to HTTPS.')
elif response.status_code == 401:
    print (json.dumps(decodedResponse['errors'][0]['detail'], sort_keys=True, indent=4))
else:
    print('Unexpected server response. Status Code:' response.status_code)
