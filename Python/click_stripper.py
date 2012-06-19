#!/usr/bin/env python
from re import findall
from sys import version_info, argv, exit
if (version_info[0] <= 2):
    from urllib import unquote
else:
    from urllib.parse import unquote

try:
    url = findall('(?iu)https?%3A%2F%2F.*?(?=&|\\Z|\\s|\\?)', argv[1])[0]
except IndexError:
    print('incompatible entry')
    exit()

print(unquote(url))

