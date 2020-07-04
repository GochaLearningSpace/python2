#! /usr/bin/env python2 
# Requesting user input
c = raw_input("Please input a integer value between 1-3 : " )
ci = int(c)
# using and to reduce the number of lines
if ( ci >= 1 and ci <= 3 ):
	print("OK: Your input is ") 
	print c
else:
	print("NG: Please input a integer value between 1-3 : " )
	print("Your input is ") 
	print c


