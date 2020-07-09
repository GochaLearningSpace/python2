#! /usr/bin/env python2

import time
t1 = time.mktime(time.localtime())
print "# time.mktime(time.localtime()) : %s", t1
time.sleep(10)
t2 = time.mktime(time.localtime())
print "# time.mktime(time.localtime()) : %s", t2

# printing how many seconds does it take.
print "# elapsed time(sec) is : " , t2-t1
 

