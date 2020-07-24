#! /usr/bin/env python2

import re

#bug text = "abc-def-ghi # This is a test sentence"
text = "abc-def-ghi-000" # This is a test sentence"

# Delete python-style comments 
num = re.sub (r'#.*$', "" , text)
print "Test setences is (1) : ", num

num = re.sub(r'\D', "" , text)
print "Test setences is (2) : ", num
