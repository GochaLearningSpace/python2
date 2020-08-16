#! /usr/bin/env python2

from Tkinter import *
top = Tk()
L1 = Label(top, text="# Modified User Name")
L1.pack(side = LEFT)
E1 = Entry(top, bd=5)
E1.pack(side = RIGHT)

top.mainloop()

