#! /usr/bin/env python2
import re

line = "Do you think Cats are smarter than Dogs ? I am not so sure.." 

matchObj = re.match(r'(.*) are (.*?) (.*?) .*' , line , re.M|re.I)

if matchObj:
	print "matchObj.group() : ", matchObj.group()
	print "matchObj.group(1) : ", matchObj.group(1)
	print "matchObj.group(2) : ", matchObj.group(2)
	print "matchObj.group(3) : ", matchObj.group(3) 
	print "matchObj.groups() : ", matchObj.groups() 
else:
	print "No match !"
