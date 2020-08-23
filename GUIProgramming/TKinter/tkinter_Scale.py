#! /usr/bin/env python2
from Tkinter import *

def select():
	selection = "Value is " + str(var.get())
	label.config(text = selection)

root = Tk()
var = DoubleVar()

label = Label(root)
label.pack()
scale = Scale ( root, variable = var )
scale.pack(anchor= CENTER)

button = Button ( root , text = "Getting Scale Value" , command = select)
button.pack(anchor = CENTER )


root.mainloop()
