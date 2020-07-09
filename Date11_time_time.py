#! /usr/bin/env python2

import time

t1 = time.time()
print "t1 is : " , t1
time.sleep(10)
t2 = time.time()
print "t2 is : " , t2

print "# elapsed time is : ", t2-t1
