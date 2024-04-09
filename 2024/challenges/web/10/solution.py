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

print("Let's see what methods are allowed on the server")
res = requests.options(url)
pprint(res.headers['Allow'])

print("\nTry a valid method\n")
print("GET request")
res = requests.get(url)
pprint(res.headers)

# try post, put, delete, patch
print("\nLet's try some methods\n")

print("Try POST request")
res = requests.post(url)
pprint(res.headers);

print("\nTry PUT request")
res = requests.put(url)
pprint(res.headers);

print("\nTry DELETE request")
res = requests.delete(url)
pprint(res.headers);

print("\nTry PATCH request")
res = requests.patch(url)
pprint(res.headers);


