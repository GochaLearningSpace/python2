#! /usr/bin/env python2

from Tkinter import *

root = Tk()

labelframe = LabelFrame(root , text = "#modi This is a LabelFrame sentence")
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text ="##modi Inside the LabelFrame")
left.pack()

root.mainloop()
