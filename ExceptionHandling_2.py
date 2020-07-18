#! /usr/bin/env python2

try:
	fh = open("test.txt","w")
	fh.write("This is my test file for exception handling!!")
except IOError:
	print "Error: cant find file or read data"
else:
	print "Written content in the file successfully"
	fh.close()
