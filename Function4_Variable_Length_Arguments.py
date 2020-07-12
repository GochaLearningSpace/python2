#! /usr/bin/env python2

def myfunc1 (arg1,*vartuple):
	print "#This prints a variable passed arguments  "
	print "# Output is "
	print arg1
	for var in vartuple:
		print var
	return 

myfunc1(10)
myfunc1(70, 60, 50)
myfunc1(70, 60, 50, 40, 30 , 20 , 10)
