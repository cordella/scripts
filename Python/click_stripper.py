#!/usr/bin/env python
from sys import version_info, argv, exit

if len(argv) < 2:
    print('must provide at least one URL')
    exit()

from re import findall

# Version agnosticism
if (version_info[0] <= 2):
    from urllib import unquote
else:
    from urllib.parse import unquote

urls = []

""" Attempt to extract real URLs from click-tracked URLs. """
for opt in argv[1:]:
    # This regular expression extracts encoded URLs
    # (ones that start with http%3A%2F%2F instead of http://)
    urls.append(findall('(?iu)https?%3A%2F%2F.*?(?=&|\\Z|\\s|\\?)', opt))

# Reduces urls to a list of strings.
urls = [i for l in urls for i in l]

print()
for url in urls:
    print(unquote(url))

