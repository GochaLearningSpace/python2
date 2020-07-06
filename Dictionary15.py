#! /usr/bin/env python2

dic ={'name': 'gocha', 'class': 'first class', 'age': 'hidden'}
print "dic['name'] : " , dic['name']
print "dic['class'] : " , dic['class'] 
print "dic['age'] : " , dic['age'] 
print "# dic: " , dic 

dic2 ={'Name': 'Gocha', 'Class': 'second class', 'Age': 'over 50'}
print "# dic2: " , dic2

dic3 = dic.update(dic2)
#print "# dic3: " , dic3
print "# dic: " , dic  # this is updated 
print "# dic.values(): " , dic.values()  # this is updated 
print "# dic2: " , dic2   
print "# dic2.values(): " , dic2.values()   



