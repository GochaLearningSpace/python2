#! /usr/bin/env python2

dic ={'name': 'gocha', 'class': 'first class', 'age': 'hidden'}
print "dic['name'] : " , dic['name']
print "dic['class'] : " , dic['class'] 
print "dic['age'] : " , dic['age'] 

dic['name'] = 'maze'
dic['class'] = 'A' 
dic['age'] = '0x23'

print "# After updating dictionary "
print "dic['name'] : " , dic['name']
print "dic['class'] : " , dic['class'] 
print "dic['age'] : " , dic['age'] 

print "dic : before del dic['class'] " , dic
del dic['class']
print "dic : after del dic['class'] " , dic
dic.clear()
print "dic : after dic.clear()" , dic

