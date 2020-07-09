#! /usr/bin/env python2

import time
#bug struct_t1 = time.strptime=("30 Nove 00" , "%d %b %y")
#struct_t1 = time.strptime("30 Nove 00" , "%d %b %y")
struct_t1 = time.strptime("30 Nov 00" , "%d %b %y")
#print "returned tuple : %s " % struct_t1
print struct_t1

# https://docs.python.org/3/library/time.html
