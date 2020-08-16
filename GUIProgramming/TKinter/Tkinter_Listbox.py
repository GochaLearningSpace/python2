#! /usr/bin/env python2

from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

Lb1 = Listbox(top)

Lb1.insert(1, "One")
Lb1.insert(2, "Two")
Lb1.insert(3, "Three")
Lb1.insert(4, "Four")
Lb1.insert(5, "Five")

Lb1.pack()
top.mainloop()
