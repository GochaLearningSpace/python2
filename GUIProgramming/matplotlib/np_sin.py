#! /usr/bin/env python2 
# https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html
# inspired by above , but modified by Gocha to fit the purpose.

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0 , 10.0 , 0.05)
s = 1 + np.sin( 2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot (t,s)

ax.set(xlabel = 'time (s)' , ylabel = 'voltge (mV)' , title = 'About as simple as it gets, folks')
ax.grid()
fig.savefig("test.png")
plt.show()


