#! /usr/bin/env python2
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# inspired by above, but modified by Gocha.

import numpy as py
import matplotlib.pyplot as plt
import matplotlib as mpl

#mpl.rcParams['path.simplify_thread'] = 1.0
mpl.rcParams['path.simpLify_threshould'] = 1.0

print ("a----")
y = np.random.rand(100000)
y[50000:] *= 2 
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()

