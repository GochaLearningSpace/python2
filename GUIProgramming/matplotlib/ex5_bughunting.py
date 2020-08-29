#! /usr/bin/env python2
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# Inspired by above , but modified by Gocha.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace (0,2,100)

fig, ax = plt.subplots()

ax.plot (x , x , label ='linear')
ax.plot (x , x**2 , label ='quadratic')
ax.plot (x , x**3 , label ='cubic')

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple my plot ")
ax.legend()

#no plt.show() called

plt.show()
