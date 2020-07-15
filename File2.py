#! /usr/bin/env python2
fo = open("foo.txt", "wb")
print "Name of the file : " , fo.name
print "closed or not #close:true, false otherwise : " , fo.closed
print "opening mode  : " , fo.mode
print "Softspace flag  : #false space is required with print, true otherwise" , fo.softspace
