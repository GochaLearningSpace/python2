#! /usr/bin/env python2

total = 0 
def sum(arg1 , arg2):
	total  = arg1 + arg2 
	print "# Inside of the Function : " , total
	return total

sum (10, 20)
print "# Outside of the Function : " , total 
sum (40, 20)
print "# Outside of the Function : " , total 

