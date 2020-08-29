#! /usr/bin/env python2

import matplotlib.pyplot as plt

x = [ 1, 2, 3, 4, 5, 6, 7,]
y = []

for each in x:
	print each
	y.append(each * each)

print x
print y 

#bug# plt.plot(x , y , 'r0') 
plt.plot(x , y , 'ro') 
plt.axis([0,10,0,50])
plt.show()
