#! /usr/bin/env python2

def sum(arg1 , arg2):
	total  = arg1 + arg2 
	print "Inside of the Function : " , total
	return total

total = sum ( 10, 20)
print "Outside of the Function : " , total 

total = sum ( 30, 20)
print "Outside of the Function : " , total 
