#! /usr/bin/env python2

from Tkinter import *

def donothing():
	filewin = Toplevel(root)
	button = Button (filewin, text = " Nothing done " )
	button.pack()

def dosomething():
	filewin = Toplevel(root)
	button = Button (filewin, text = " ### Something done " )
	button.pack()

root = Tk()
menubar = Menu(root)

filemenu = Menu ( menubar, tearoff=0)
filemenu.add_command(label="Menu1" , command=donothing)
filemenu.add_command(label="Menu2" , command=donothing)
filemenu.add_command(label="Menu3" , command=donothing)
filemenu.add_command(label="Menu4" , command=donothing)
filemenu.add_command(label="Menu5" , command=donothing)

filemenu.add_separator()

filemenu.add_command(label="quit" , command=root.quit)
menubar.add_cascade(label="Menus", menu=filemenu)

root.config(menu=menubar)
root.mainloop()

