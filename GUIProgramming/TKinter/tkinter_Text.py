#! /usr/bin/env python2

from Tkinter import *

def onclick():
	pass

root = Tk()
text = Text(root)

text.insert(INSERT , "Hi....")
text.insert(END , "Good Bye")

text.pack()

text.tag_add("here", "1.0" , "11.4")
text.tag_add("start", "1.8" , "1.13")

text.tag_config("here", background="red" , foreground="blue")
text.tag_config("start", background="black" , foreground="green")

root.mainloop()

