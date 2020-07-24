#! /usr/bin/env python2
import re

line = "Cats are smater than dogs "

matchObj = re.match( r'dogs', line , re.M|re.I)
if matchObj:
	print "match --> matchObj.group() : " , matchObj.group()
else:
 	print "#re.match : No match !! "

searchObj = re.search(r'dogs', line  , re.M|re.I)

if searchObj:
	print "search --> searchObj.group() : ", searchObj.group()
else:
	 
	print "#re.search : Nothing found !"
