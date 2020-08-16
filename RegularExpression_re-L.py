#! /usr/bin/env python2

import re
text = "abc\Wdef\Wghi # This is a test sentence"

num = re.search ('a.*$', text , re.L)
print "Test setences is (1) : ", num.group() 

