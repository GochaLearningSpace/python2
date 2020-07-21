#! /usr/bin/env python2

a = 40
b = a
c = [b]

print "a :"  , a 
print "b :"  , b 
print "c :"  , c 

del a
b = 100
c[0] = -1

print "#after , del a , b=100 , c[0] =-1 " 
 
print "a :"  , a 
print "b :"  , b 
print "c :"  , c 
