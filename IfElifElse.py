#! /usr/bin/env python2 
# Requesting user input
c = raw_input("Please input a integer value between 1-3 : " )

if (c < 1):
	print("Please input a integer value between 1-3 : " )
	print("Your input is ") 
	print c
elif (c > 3):
	print("Please input a integer value between 1-3 : " )
	print("Your input is ") 
	print c
else:
	print("This should not be called " )


