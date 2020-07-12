#! /usr/bin/env python2

#bug# def myfunc1 (name="chome",age ):
def myfunc1 (name="chome",age = 8):
	print "#called in myfunc1  "
	print "# name is   ", name
	print "# age is   ", age 
	return 

myfunc1()
myfunc1("Tama", 3)
myfunc1("Gocha", 4)
