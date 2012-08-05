#!/usr/bin/env python
#
# Based on http://www.unix.com/44705-post4.html

import os, sys, datetime
import time


values = sys.argv[1:]

for value in values:
    print(value + " --> " + datetime.datetime.fromtimestamp(float(value)).strftime("%Y-%d-%m %H:%M:%S"))

