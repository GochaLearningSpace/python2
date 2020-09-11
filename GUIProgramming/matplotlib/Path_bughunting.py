#! /usr/bin/env python2
# https://matplotlib.org/3.2.1/tutorials/advanced/path_tutorial.html
# inspired by above but modified by Gocha for purpose

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

verts = [
	(0. , 0.),
	(0. , 1.),
	(1. , 1.),
	(1. , 0.),
	(0. , 0.),
]

codes = [
	Path.MOVETO,
	Path.LINETO,
	Path.LINETO,
	Path.LINETO,
	Path.CLOSEPOLY,
]

path = Path(verts , codes)

fig , ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='orange',lw=2)
ax.add_patch(patch)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
plt.show()
