#!/usr/bin/env python3

import requests

def print_response(response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

# Define the URL of the website you want to scrape
url = 'http://web-06.challs.olicyber.it/'

response = requests.get(url + '/token')
cookies = response.cookies

response = requests.get(url + '/flag', cookies=cookies)
print_response(response)

# or
s = requests.Session()
s.get(url + '/token')
response = s.get(url + '/flag')
print_response(response)



