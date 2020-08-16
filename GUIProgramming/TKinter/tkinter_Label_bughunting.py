#! /usr/bin/env python2
from Tkinter import *

root = Tk()
var = StringVar()

label = Label ( root, textvariable=var , relief=RAISED )
var.set("#modified How are you ? ")
label.pack()

root.mainloop()
