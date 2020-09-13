#! /usr/bin/env python2
# https://matplotlib.org/gallery/misc/table_demo.html
# Inspired by above url, but modified by Gocha for purpose.

import numpy as np
import matplotlib.pyplot as plt

dat = [
	 [ 66386, 174296, 75131, 577908, 32015], # lowest row
	 [ 58230, 381139, 78045,  99308, 160454], # 2nd lowest row
	 [ 89135, 80552,  152558, 497981, 603535], # middle row
	 [ 78415, 81858,  150565, 1923263, 69638], # 2nd from highest 
	 [ 139361, 331509,  343164, 781380, 52269] # highest row
	]

columns = ('Freeze' , 'Wind' , 'Flood' , 'Quake' , 'Hail')
rows = ['%d year' % x for x in (100,50,20,10,5)]

values = np.arange( 0, 2500 ,500)
value_increment = 1000

colors = plt.cm.BuPu(np.linspace(0,0.5, len(rows))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []

for row in range (n_rows):
	plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
	y_offset = y_offset + data[row]
	cell_text.appen(['%1.1f' % (x/1000.0) for x in y_offset])

colors = color[::-1]
cell_text.reverse()

the_table = plt.table(cellText = cell_text, 
			rowLabels = rows,	
			rowColours = colors,	
			colLabels = columns,	
			loc = 'bottom' )

plt.subplots_adjust(left = 0.2 , bottom = 0.2)
plt.ylabel("Loss in ${0}'s".format(value_increment))
plt.yticks(values * value_increment, ['%d' %val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')

plt.show()

