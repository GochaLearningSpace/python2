#! /usr/bin/env python2
print "input file name: "
file_name = raw_input()
fo = open(file_name, "wb")
print "Name of the file : " , fo.name
fo.write("Python is convenient. \n yes convenient. \n")
fo.close()
