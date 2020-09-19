#! /usr/bin/env python3
# https://matplotlib.org/examples/animation/bayes_update.html
# inspired by above but modified by Taka

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
from matplotlib.animation import FuncAnimation

class UpdateDist(object):
	#bug def __inif__(self, ax , prob=0.5):
	def __init__(self, ax , prob=0.5):
		self.success = 0 
		self.prob = prob
		self.line , = ax.plot([],[],'k-')
		self.x = np.linspace(0,1,200)
		self.ax = ax
		#bug self.ax_set_xlim(0,1) 
		self.ax.set_xlim(0,1) 
		#bug self.ax_set_ylim(0,15) 
		self.ax.set_ylim(0,15) 
		self.ax.grid(True)
		self.ax.axvline(prob, linestyle ='--', color='black')

	def init(self):
		self.succes =0
		self.line.set_data([],[])
		return self.line,

	def __call__(self, i):
		if i == 0:
			return self.init()	

		if np.random.rand(1,) < self.prob:
			self.success += 1
		#bug y - ss.beta.pdf(self.x , self.success + 1 , ( i -self.success ) + 1)
		y = ss.beta.pdf(self.x , self.success + 1 , ( i -self.success ) + 1)
		self.line.set_data(self.x , y)
		return self.line,

fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud , frames = np.arange(100), init_func = ud.init, interval = 100, blit=True)
plt.show()
