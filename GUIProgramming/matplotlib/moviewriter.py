#! /usr/bin/env python2
# https://matplotlib.org/examples/animation/moviewriter.html
# Inspired by above. Modified by Gocha for purpose.

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

FFMpegWriter = animation.writers['ffmpeg']
metadata = dict(title='Movie Test' , artist = 'Matplotlib', comment = 'Movie Support !')
writer = FFMpegWriter ( fps = 15 , metadata =metadata)

fig = plt.figure()
l, = plt.plot ( [] , [], 'k-o')

plt.xlim(-5,5)
plt.ylim(-5,5)

x0 , y0 = 0  , 0
with writer.saving(fig, "writer_test.mp4", 100):
	for i in range(100):
		x0 += 0.1 * np.random.randn()  
		y0 += 0.1 * np.random.randn()  
		l.set_data(x0, y0)
		writer.grab_frame()
