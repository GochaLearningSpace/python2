#! /usr/bin/env python2

import re
text = "abc-def-ghi # This is a test sentence"

num = re.search (r'd.*$', text , re.I)
print "Test setences is (1) : ", num.group() 

