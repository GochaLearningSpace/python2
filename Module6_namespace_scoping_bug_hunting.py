#! /usr/bin/env python2
Number = 1000
def AddNumber():
	Number = Number + 1 
	#bug2#global Number = Number + 1 
	#global Number 
	#Number = Number + 1 

print Number 
AddNumber()
print Number 
