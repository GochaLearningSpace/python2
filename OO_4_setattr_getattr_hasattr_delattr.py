#! /usr/bin/env python2

class Employee:
 empCount = 0

 def __init__(self, name , salary):
	self.name = name
	self.salary = salary 
	Employee.empCount += 1

 def displayCount(self):
	print "Total Employee %d" % Employee.empCount

 def displayEmployee(self):
	print "Name : ", self.name , ", Salary: " , self.salary

emp1 = Employee("Zara",2000)
emp2 = Employee("Manni",5000)
emp3 = Employee("Tama",6000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

print "Total Employee %d" % Employee.empCount
print "hasattr(emp1, 'age')", hasattr(emp1, 'age')
print "setattr(emp1, 'age', 8)", setattr(emp1, 'age', 8)
print "getattr(emp1, 'age')", getattr(emp1, 'age')
print "hasattr(emp1, 'age')", hasattr(emp1, 'age')
print "delattr(emp1, 'age')", delattr(emp1, 'age')
print "hasattr(emp1, 'age')", hasattr(emp1, 'age')

