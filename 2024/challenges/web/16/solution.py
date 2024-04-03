#!/usr/bin/env python3

import requests, sys, re
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin

# Define the URL of the website you want to scrape
url = 'http://web-16.challs.olicyber.it/'

res = requests.get(url);

# visited pages
pages = []

def find_flag(url):
    if url in pages: 
        print ("Already visited: ", url)
        return
    print(url)
    pages.append(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    print (soup.h1.string)
    if (re.compile(r'flag\{.*\}').search(soup.h1.string)): sys.exit()
    for tag in soup.find_all(['a']):
        find_flag(urljoin(url, tag['href']))
    

res = requests.get(url);
soup = BeautifulSoup(res.text, 'html.parser')
for tag in soup.find_all(['a']):
    find_flag(urljoin(url, tag['href']))