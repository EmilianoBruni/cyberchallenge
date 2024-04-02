#!/usr/bin/env python3

import requests

# Define the URL of the website you want to scrape
url = 'http://web-04.challs.olicyber.it/users'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the JSON source code
    print('Default server response:\n')
    print('========================\n');
    print(response.text)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)

# request with accept header application/xml

accept_header = { 'Accept': 'application/xml' }

response = requests.get(url, headers=accept_header)

if response.status_code == 200:
    # Print the XML source code
    print('XML server response:\n')
    print('========================\n');
    print(response.text)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
