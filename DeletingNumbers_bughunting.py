#! /usr/bin/env python2

s1 = "hello "
s2 = "world " 

s3 = s1 + s2 
print "s1 : " , s1
print "s2 : " , s2
print "s3 : " , s3

#delete s1
del s1
#delete s2 
del s2 

#print "s1 : " , s1
#print "s2 : " , s2
print "s3 after del s1 del s2 : " , s3
