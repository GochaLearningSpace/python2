#! /usr/bin/env python2
class Parent:
 def __init__( self, x=0 , y=0):
	self.x = x
	self.y = y 
	self.name = "Parent"
	print "#Calling parent __init__, calling constructor"
 def __del__(self):
	class_name = self.__class__.__name__
	print class_name  , "#Calling Parent destructor , destroyed " 

class Child(Parent):
 def __init__(self):
	print "Calling child constructor "
	self.name = "Child"
 def __del__(self):
	print "Calling child destructor "
 def __cmp__(self, another):
	print "Calling __cmp__ in child class "
	if self.name < another.name :
		return -1
	elif self.name > another.name:
		return 1
	else: 
		return 0
c = Child()
c1 = Child()
c.__cmp__(c1)
print( "# c.__cmp__(c1) : ",  c.__cmp__(c1))
print( "# c > c1 : ",  c > c1)
print( "# c < c1 : ",  c < c1)
print( "# c == c1 : ",  c == c1)
print( "# c != c1 : ",  c != c1)

