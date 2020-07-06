#! /usr/bin/env python2

dic ={'name': 'gocha', 'class': 'first class', 'age': 'hidden'}
print "dic['name'] : " , dic['name']
print "dic['class'] : " , dic['class'] 
print "dic['age'] : " , dic['age'] 

print "# dic: " , dic 
print "# len(dic): " , len(dic)
print "# str(dic): " , str(dic)
print "# type(dic): " , type(dic)

dic1 = dic.fromkeys(dic, 10)
print "###### dic1.fromkeys(dic,10)  ##### " 
print "# dic1: " , dic1 
print "# len(dic1): " , len(dic1)
print "# str(dic1): " , str(dic1)
print "# type(dic1): " , type(dic1)

dic2 = dic.fromkeys(dic)
print "###### dic.fromkeys(dic)  ##### " 
print "# dic2: " , dic2
print "# len(dic2): " , len(dic2)
print "# str(dic2): " , str(dic2)
print "# type(dic2): " , type(dic2)

