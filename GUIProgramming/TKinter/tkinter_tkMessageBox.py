#! /usr/bin/env python2

import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
	tkMessageBox.showinfo("#modi Say Hello" , "#modi Hello World")

B1 = Tkinter.Button(top, text = "Say Hello2" , command=hello)
B1.pack()

top.mainloop()
