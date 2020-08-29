#! /usr/bin/env python2

from Tkinter import *
m1 = PanedWindow()

#bug# m1.pack(fill=Both, expand=1)
m1.pack(fill=BOTH, expand=1)

#bug# left = Label(m1 , test = "left")
left = Label(m1 , text = "left")

#bug#right = Label(m1 , test = "right")
right = Label(m1 , text = "right")

m1.add(left)
m1.add(right)

mainloop()


