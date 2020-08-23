#! /usr/bin/env python2
# referring below site, but modified for this purpose.
# https://www.tutorialspoint.com/python/tk_radiobutton.htm

from Tkinter import *
root = Tk()
label = Label(root)

var = IntVar()

def select():
	selection = "Your selection is " + str(var.get())
	label.config(text = selection)


R1 = Radiobutton ( root, text = "option 1", variable = var , value = 1, command=select)
R1.pack(anchor = W)

R2 = Radiobutton ( root, text = "option 2", variable = var , value = 2, command=select)
R2.pack(anchor = W)

R3 = Radiobutton ( root, text = "option 3", variable = var , value = 3, command=select)
R3.pack(anchor = W)
label.pack()

root.mainloop()

