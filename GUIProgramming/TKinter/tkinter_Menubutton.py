#! /usr/bin/env python2

from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

mb = Menubutton ( top , text="fruits", relief=RAISED)
mb.grid()
mb.menu = Menu (mb , tearoff =0 )
mb["menu"] = mb.menu

appleVar = IntVar()
bananaVar = IntVar()
orangeVar = IntVar()

mb.menu.add_checkbutton ( label = "apple", variable=appleVar)
mb.menu.add_checkbutton ( label = "banana", variable=bananaVar)
mb.menu.add_checkbutton ( label = "orange", variable=orangeVar)

mb.pack()
top.mainloop()

