#! /usr/bin/env python2
print "input file name: "
#file_name = input()
file_name = raw_input()
print file_name
fo = open(file_name, "wb")
print "Name of the file: " , fo.name
fo.close()
