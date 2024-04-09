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
print("Login to the resource and got a  csrf token:")
req = s.post(f'{url}login', json={"username": "admin", "password": "admin"})

token = req.json()['csrf']
print(f"{token}\n")
flag = ''

for i in range(4):
    print(f"Getting flag piece {i} with csrf token: {token}\n")
    req = s.get(f'{url}flag_piece', params={ "index": i, "csrf": token })
    print_response(req)
    token = req.json()['csrf']
    flag_piece = req.json()['flag_piece']
    flag += flag_piece
    print(f"Flag piece {i}: {flag_piece}. New token: {token}\n")

print (f"Full flag: {flag}")