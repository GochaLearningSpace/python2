#! /usr/bin/env python2

list1 = [0,1,2,3,4]
list2 = [5,6,7,8,9]

print "#list1 is : ", list1
print "#list2 is : ", list2

list3 = list1 + list2

print "#list3 is : ", list3

list4 = list1.extend(list2)

print "# list4 = list1.extend(list2)"

print "#list1 is : ", list1
print "#list2 is : ", list2
print "#list3 is : ", list3
print "#list4 is : ", list4
