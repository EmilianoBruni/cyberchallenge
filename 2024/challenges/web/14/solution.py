#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup, Comment

def has_comment(tag):
    for content in tag.contents:
        if isinstance(content, Comment):
            return True
            break
    return False

# Define the URL of the website you want to scrape
url = 'http://web-14.challs.olicyber.it/'

res = requests.get(url);
soup = BeautifulSoup(res.text, 'html.parser')
flag = '';
for tag in soup.find_all(has_comment):
    for content in tag.contents:
        if isinstance(content, Comment):
            print (content)


