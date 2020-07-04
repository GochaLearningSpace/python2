#! /usr/bin/env python2 
# Requesting user input
c = raw_input("Please input a integer value between 1-3 : " )

# using or to reduce the number of lines
if (c < 1 or c > 3 ):
	print("# NG:Please input a integer value between 1-3 : " )
	print("Your input is ") 
	print c
else:
	print("# OK : Your input is " )
	print c


