#! /usr/bin/env python2
from Tkinter import *

root = Tk()
var = StringVar()

label = Message (root , textvariable=var , relief = RAISED )

var.set ("### modified Good afternoon, how are you ?")
label.pack()

root.mainloop()

