#!/usr/bin/env python3

import requests

def print_response(response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

# Define the URL of the website you want to scrape
url = 'http://web-08.challs.olicyber.it/login'

data = { 'username': 'admin', 'password': 'admin' }
res = requests.post(url, data=data)
print_response(res)


