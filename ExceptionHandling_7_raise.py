#! /usr/bin/env python2

def myfunc (level):
	if level < 1 :
		raise "Invalid level", level

print " Please input a number which is over 1 "
my_input = raw_input()

try:
	myfunc(int(my_input))
except "Invalid Level":
	print "The argument is not appropriate \n", Argument




