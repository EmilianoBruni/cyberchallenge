#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'http://web-13.challs.olicyber.it/'

res = requests.get(url);
soup = BeautifulSoup(res.text, 'html.parser')
flag = '';
for tag in soup.find_all('span', "red"):
    flag += tag.text

print('flag{' + flag + '}');


