#!/usr/bin/env python3

import requests

def print_response(response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

# Define the URL of the website you want to scrape
url = 'http://web-11.challs.olicyber.it/'

s = requests.Session()
req = s.post(f'{url}login', json={"username": "admin", "password": "admin"})

token = req.json()['csrf']
flag = ''

for i in range(4):
    req = s.get(f'{url}flag_piece', params={ "index": i, "csrf": token }, cookies=req.cookies)
    print_response(req)
    token = req.json()['csrf']
    flag += req.json()['flag_piece']
    
print(flag)