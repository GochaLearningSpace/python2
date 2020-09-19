#! /usr/bin/env python2 
# https://matplotlib.org/gallery/animation/basic_example.html
# inspired by above , modified by Gocha.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num, data , line):
	line.set_data(data[...,  :num])
	return line,

fig1 = plt.figure()

np.random.seed(123456789)
data = np.random.rand(2,25)
l, = plt.plot([],[], 'r-')
plt.xlim=(0,1)
plt.ylim=(0,1)
plt.xlabel('x')
plt.title('test')

line_ani = animation.FuncAnimation(fig1, update_line, 25 , fargs = (data,l), interval = 50, blit=True)
plt.show()



