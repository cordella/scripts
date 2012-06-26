#!/usr/bin/env python
from sys import argv
from re import findall

f = open(argv[1], 'rb')
t = findall('\w+?.bsp', f.read())
f.close()
print(t)
