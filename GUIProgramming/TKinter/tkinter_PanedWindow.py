#! /usr/bin/env python2

from Tkinter import *
m1 = PanedWindow()

m1.pack(fill=BOTH, expand=1)

left = Label(m1 , text = "left")
m1.add(left)


m2 = PanedWindow(m1, orient= VERTICAL)
m1.add(m2)

top = Label(m2 , text = "top")
bottom = Label(m2 , text = "bottom")

m2.add(top)
m2.add(bottom)


m3 = PanedWindow(m2, orient= VERTICAL)
m2.add(m3)
right = Label(m3 , text = "right")
m3.add(right)

mainloop()


