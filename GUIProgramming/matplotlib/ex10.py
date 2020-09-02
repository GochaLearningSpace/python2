#! /usr/bin/env python2
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# inspired by above , but modified by Gocha to make it fit this purpose.

import matplotlib.pyplot as plt
import numpy as np

def my_plotter(ax , data1 , data2, param_dict):
	out = ax.plot(data1 , data2 , **param_dict)
	return out

data1 , data2 , data3, data4 = np.random.randn(4,100)
fig , (ax1 , ax2 ) = plt.subplots(1,2)
my_plotter(ax1 , data1 , data2 , {'markter': 'x'})
my_plotter(ax2 , data3 , data4 , {'markter': 'o'})
