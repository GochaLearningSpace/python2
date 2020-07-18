#! /usr/bin/env python2

try:
	fh = open("test.txt","w")
	fh.write("This is my test file for exception handling!!")
finally:
	#print "Error cannot find file or read data"
	print "this is called in the end"
