#! /usr/bin/env python2

from Tkinter import *
import tkMessageBox
import Tkinter

top = Tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

C1 = Checkbutton( top, text = "item one 1", variable = CheckVar1, onvalue = 1 , offvalue = 0, height =20 , width = 20 , fg="pink", bg="black")
C2 = Checkbutton( top, text = "item two 2", variable = CheckVar2, onvalue = 1 , offvalue = 0, height =20 , width = 20 , fg="green" ,bg="white")

C1.pack()
C2.pack()
top.mainloop()


