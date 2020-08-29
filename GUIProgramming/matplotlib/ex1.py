#! /usr/bin/env python3

import matplotlib.pyplot as plt

labels = ['G1' , 'G2' , 'G3', 'G4' , 'G5']
a_means = [ 20, 35 , 30 , 35 ,27]
b_means = [25, 33, 30 , 39 , 28]
a_std = [ 2,3,4,1,2]
b_std = [ 3,5,2,3,3]

width = 0.5 

fig , ax = plt.subplots()

ax.bar(labels, a_means, width , yerr = a_std , label = 'A')
#ax.bar(labels, b_means, width , yerr = b_std , bottom- a_means, label = 'B')
ax.bar(labels, b_means, width , yerr = b_std , bottom = a_means, label = 'B')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()
