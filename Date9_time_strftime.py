#! /usr/bin/env python2

import time
t = (2009 , 2, 17 , 17, 3, 38, 1, 48,0)
print "t is : ", t 
t1 = time.mktime=(t)
print "t1 = time.mktime(t) is : ", t1
print time.strftime("%b, %d, %Y, %H:%M:%S", time.gmtime(t1))
 
 

