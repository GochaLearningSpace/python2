#! /usr/bin/env python2

import matplotlib.pyplot as plt
import numpy as np

def my_plotter(ax, data1 , data2, param_dict):
	out = ax.plot(data1 , data2, **param_dict)
	return out

data1 , data2 , data3, data4 = np.random.randn(4,500)
fig , ax = plt.subplots(1,1)
my_plotter(ax, data1, data2, {'marker' : 'x'})
plt.show()
