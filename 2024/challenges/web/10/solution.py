#!/usr/bin/env python3

import requests
from pprint import pprint

def print_response(response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

# Define the URL of the website you want to scrape
url = 'http://web-10.challs.olicyber.it/'

res = requests.options(url)
pprint(res.headers['Allow'])

# try post, put, delete, patch
res = requests.post(url)
pprint(res.headers);

res = requests.put(url)
pprint(res.headers);

res = requests.delete(url)
pprint(res.headers);

res = requests.patch(url)
pprint(res.headers);


