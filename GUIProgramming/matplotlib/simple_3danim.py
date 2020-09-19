#! /usr/bin/env python2
# https://matplotlib.org/examples/animation/simple_3danim.html
# inspired by above, modified by Gocha.

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

def Gen_RandLine(length, dims=2):
	lineData = np.empty(( dims, length ))
	lineData[:, 0] = np.random.rand( dims)
	
	for index in range( 1, length)  :
		step = (( np.random.rand(dims) - 0.5) * 0.1)
		lineData[ :, index ] = lineData[:, index -1 ] + step
	return lineData

def update_lines(num , dataLines, lines):
	for line, data in zip ( lines, dataLines):
		line.set_data(data[0:2, : num])
		line.set_3d_properties(data[2, : num])
	return lines

fig = plt.figure()
ax = p3.Axes3D(fig)

data = [ Gen_RandLine(25,3) for index in range(50)]
#bug lines = [ ax.plot(dat[0,0:1] , dat[1, 0:1])[0] for dat in data]
lines = [ ax.plot(dat[0,0:1] , dat[1, 0:1] , dat[2, 0:1] )[0] for dat in data]

ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('X')
ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('Y')
ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('Z')
ax.set_title('3D Test')
line_ani = animation.FuncAnimation(fig, update_lines, 25 , fargs=(data,lines), interval=50  ,blit = False)
plt.show()

	
