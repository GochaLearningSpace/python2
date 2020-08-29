#! /usr/bin/env python2

import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
	tkMessageBox.showinfo("Say Hello" , "Hello World")

#bug# B1 = Tkinter.Button(top, text = "Say Hello" . command=hello)
B1 = Tkinter.Button(top, text = "Say Hello" , command=hello)
B1.pack()

top.mainloop()
