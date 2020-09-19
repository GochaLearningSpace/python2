#! /usr/bin/env python2
# https://matplotlib.org/examples/animation/simple_anim.html
# inspired by above ,modified by Gocha.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi , 0.01)
line, = ax.plot(x , np.tan(x))

def animate(i):
	line.set_ydata(np.tan(x + 1 / 10.0))
	return line,

def init():
	line.set_ydata(np.ma.array(x,mask = True))
	return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1,200 ) , init_func= init, interval =25, blit=True)
plt.show()
