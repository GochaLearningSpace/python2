#! /usr/bin/env python2

try:
	fh = open("test.txt","w")
	try:
		fh.write("This is my test file for exception handling!!")
	finally:
		print "Going to close the file"
		fh.close()
except IOError:
	print "this is called in the end"
