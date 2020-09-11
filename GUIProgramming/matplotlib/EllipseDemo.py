#! /usr/bin/env python2
# https://matplotlib.org/gallery/shapes_and_collections/ellipse_demo.html
# Inspired by above , but modified by Gocha.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

np.random.seed(13456789)

NUM =5550

el=[Ellipse(xy=np.random.rand(2)*10, width=np.random.rand(), height = np.random.rand(), angle=np.random.rand() * 360) for i in range(NUM)]

fig , ax = plt.subplots(subplot_kw={'aspect': 'equal'})
for e in el:
	ax.add_artist(e)
	e.set_clip_box(ax.bbox)
	e.set_alpha(np.random.rand())
	e.set_facecolor(np.random.rand(3))

ax.set_xlim(0,10)	
ax.set_ylim(0,10)	

plt.show()

