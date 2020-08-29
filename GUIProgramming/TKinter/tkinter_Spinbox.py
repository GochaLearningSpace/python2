#! /usr/bin/env python2

from Tkinter import *
master = Tk()

w = Spinbox(master , from_=-10 , to=20)
w.pack()

mainloop()
