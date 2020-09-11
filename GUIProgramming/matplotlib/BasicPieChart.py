#! /usr/bin/env python2
# https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
# Inspired by Above but modified by Gocha for purpose.

import matplotlib.pyplot as plt
labels = 'Cats' , 'Dogs' , 'Snakes', 'Flogs'
sizes = [15,30,45,60]
explode = (0,0.1, 0,0)

fig1 , ax1 = plt.subplots()
ax1.pie(sizes, explode=explode , labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
