#! /usr/bin/env python2

class JustCounter:
 __secretCount = 0

 def count(self):
	self.__secretCount  += 1
	print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()

#bug not allowed# print counter.__secretCount
print counter._JustCounter__secretCount

