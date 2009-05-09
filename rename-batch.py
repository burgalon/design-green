#!/usr/local/bin/python

# Python Rename File 1.0 
# Author: Douglas Palovick
# License: GPL http://www.gnu.org/licenses/gpl.txt

import re, os
rxin = raw_input('enter a regex to search for:\n')
foo = re.compile(rxin)
newname = raw_input('enter a new base name:\n')
a = 0
for fname in os.listdir(os.getcwd()):
    allowed_name = re.compile(rxin).match
    if allowed_name(fname):
        # newfname = string.lower(re.sub(foo,
                                   # '', fname))
        # b = (newname + str(a))
        a += 1
        c = os.path.splitext(fname)
        b = (newname + str(a) + c[1])
        os.rename(fname, b)
