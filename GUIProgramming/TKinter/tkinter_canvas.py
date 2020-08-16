#! /usr/bin/env python2 
# inspired by below 
# https://www.tutorialspoint.com/python/tk_canvas.htm

import Tkinter
top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10 , 50 , 240 , 250

arc = C.create_arc(coord , start = 150, extent = 0 , fill = "green")
C.pack()
top.mainloop()
