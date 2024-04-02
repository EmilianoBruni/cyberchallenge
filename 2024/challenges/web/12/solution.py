#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'http://web-12.challs.olicyber.it/'

res = requests.get(url);
soup = BeautifulSoup(res.text, 'html.parser')
for tag in soup.find_all('pre'):
    print(tag.text)



