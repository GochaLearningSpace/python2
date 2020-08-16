#! /usr/bin/env python2
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def hellocb():
	tkMessageBox.showinfo("Hello Python", "hello world")

B= Tkinter.Button(top , text = "HELLO#########", command = hellocb)

B.pack()
top.mainloop()
