#!/usr/bin/env python3.2
from re import findall
from sys import argv, exit
from urllib.parse import unquote

try:
    url = findall('(?iu)https?%3A%2F%2F.*?(?=&|\\Z|\\s)', argv[1])[0]
except IndexError:
    print('incompatible entry')
    exit()

url = unquote(url)

print(url)

