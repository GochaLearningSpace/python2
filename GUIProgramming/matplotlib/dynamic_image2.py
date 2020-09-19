#! /usr/bin/env python2
# https://matplotlib.org/examples/animation/dynamic_image2.html
# Inspired by above, but modified by Gocha for purpose.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

def f(x,y):
	return np.sin(x) + np.cos(y)

x = np.linspace(0, 2* np.pi , 120)
y = np.linspace(0, 2* np.pi , 100).reshape(-1,1)

ims = []
for i in range(60):
	x += np.pi/150
	y += np.pi/200
	im = plt.imshow(f(x,y), animated = True)
	ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval =50, blit = True, repeat_delay= 1000)
ani.save("dynamic_images2_b.mp4")
plt.show()
 
