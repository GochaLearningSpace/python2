#! /usr/bin/env python2
class MyVector:
 def __init__( self, a , b):
	self.a = a 
	self.b = b 
	print "#Calling MyVector __init__, calling constructor"
 def __del__(self):
	class_name = self.__class__.__name__
	print class_name  , "#Calling MyVector destructor , destroyed " 
 def __str__(self):
	return  "#Vector (%d , %d ) " % (self.a, self.b)   
 def __add__(self,other):
	return  MyVector (self.a + other.a , self.b + other.b)  

v1 = MyVector(2,10)
v2 = MyVector(5,-2)
print "# v1 + v2 = " , (v1 + v2)

v3 = MyVector(2,20)
v4 = MyVector(15,-20)
print "# v3 + v4 = " , (v3 + v4)
