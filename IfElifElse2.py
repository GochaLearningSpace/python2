#! /usr/bin/env python2 
# Requesting user input

c = raw_input("Please input a integer value between 1-3 : " )
ci = int(c)

# using or to reduce the number of lines
if (ci < 1 or ci > 3 ):
	print("# NG:Please input a integer value between 1-3 : " )
	print("Your input is ") 
	print ci
else:
	print("# OK : Your input is " )
	print ci


