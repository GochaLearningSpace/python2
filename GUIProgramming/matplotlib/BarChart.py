#! /usr/bin/env python2
# https://matplotlib.org/gallery/lines_bars_and_markers/barh.html
# Inspired by above but modified by Taka.

import matplotlib.pyplot as plt
import numpy as np

# Setting random seed for reproducibility
np.random.seed(100000)

plt.rcdefaults()
fig, ax = plt.subplots()

people = ('Alice' , 'Ben' , 'Chris' , 'Dave' , 'Elvin' , 'Flay') 
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr = error, align = 'center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today')

plt.show()

