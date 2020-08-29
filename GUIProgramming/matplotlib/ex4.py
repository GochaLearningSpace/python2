#! /usr/bin/env python2
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# Inspired by above , modified by Gocha

import matplotlib.pyplot as plt
import numpy as np

fig , ax = plt.subplots()
x = [1,2,3,4,5,6,7,8]
y = [1,4,2,3,8,20,10,-10]

ax.plot( x , y)
plt.show()
