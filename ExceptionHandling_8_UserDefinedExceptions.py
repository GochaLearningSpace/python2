#! /usr/bin/env python2

class MyClassError(RuntimeError):
	def __init__(self,arg):
		self.args = arg 
try:
	raise MyClassError("---- Class Error")

except MyClassError,e:
	print e.args 




