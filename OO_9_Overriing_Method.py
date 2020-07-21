#! /usr/bin/env python2
class Parent:
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
 def __init__(self):
	print "Calling child constructor "
 def myMethod(self):
	print "Calling myMethod in child class"
 def childMethod(self):
	print "Calling child method " 
 def __del__(self):
	print "Calling child destructor "

c = Child()
c.childMethod()
c.myMethod()
c.setAttr(200)
c.getAttr()

print c 
