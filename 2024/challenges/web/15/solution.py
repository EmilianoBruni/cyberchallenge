#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup, Comment
import re

# Define the URL of the website you want to scrape
url = 'http://web-15.challs.olicyber.it/'

res = requests.get(url);
soup = BeautifulSoup(res.text, 'html.parser')
for tag in soup.find_all(['link','script']):
    if tag.name == 'link':
        if 'stylesheet' in tag['rel']:
            res = requests.get(url + tag['href'])
            # search for flag in res.text
            m=re.search(r'flag\{.*\}', res.text)
            if m: print(m.group(0))
    if tag.name == 'script':
        res = requests.get(url + tag['src'])
        # search for flag in res.text
        m=re.search(r'flag\{.*\}', res.text)
        if m: print(m.group(0))

