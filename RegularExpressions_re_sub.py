#! /usr/bin/env python2

import re

#text = "abc-def-ghi # This is a test sentence"
text = "111-234-56789A" # This is a test sentence"

# Delete python-style comments 
num = re.sub (r'#.*$', "" , text)
print "Test setences is (1) : ", num

# Remove anything other than digits
num = re.sub(r'\D', "" , text)
print "Test setences is (2) : ", num
