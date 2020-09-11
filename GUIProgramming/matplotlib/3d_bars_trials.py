#! /usr/bin/env python3
# https://matplotlib.org/gallery/mplot3d/3d_bars.html#sphx-glr-gallery-mplot3d-3d-bars-py
# inspired by above, but modified by Gocha for purpose.

import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#fig = plt.figure(figsize = (8.3))
fig = plt.figure(figsize = (8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

_x = np.arange(4)
_y = np.arange(5)
_xx , _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x,y,bottom,width , depth, top, shade=True)
ax1.set_title('It\'s shaded version')

ax2.bar3d(x,y,bottom,width , depth, top, shade=False)
ax2.set_title('It\'s non-shaded version')

plt.show()

