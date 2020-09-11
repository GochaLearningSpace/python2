#! /usr/bin/env python2
# https://matplotlib.org/gallery/images_contours_and_fields/pcolormesh_levels.html
# Inspired by Above but modified by Gocha.

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

np.random.seed(123456780)
Z= np.random.rand(6,10)
x = np.arange(-0.5 , 10, 1)
y = np.arange(4.5 , 11, 1)

fig, ax = plt.subplots()
ax.pcolormesh(x , y , Z)

plt.show()
