#! /usr/bin/env python2
class Parent:
 name = "parent 1"
 def __init__( self, x=0 , y=0):
	self.x = x
	self.y = y 
	print "#Calling parent __init__, calling constructor"
 def myMethod(self):
	print "Calling myMethod in parent class"
 def setAttr(self,attr):
	Parent.parentAttr = attr
 def getAttr(self):
	print "Parent Attribute : ", Parent.parentAttr
 def __del__(self):
	class_name = self.__class__.__name__
	print class_name  , "#Calling Parent destructor , destroyed " 

class Child(Parent):
 name = "child 1"
 def __init__(self):
	print "Calling child constructor "
 def myMethod(self):
	print "Calling myMethod in child class"
 def childMethod(self):
	print "Calling child method " 
 def __del__(self):
	print "Calling child destructor "
 def __repr__(self):
	print "Calling repr in child class "
 def __str__(self):
	print "Calling str in child class "
	return self.name

c = Child()
c.childMethod()
c.myMethod()
c.setAttr(200)
c.getAttr()
c.__repr__()
c.__str__()
print( "# c.__repr__() : ",  c.__repr__())
print( "# c.__str__() : ",  c.__str__())
print c

