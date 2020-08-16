#! /usr/bin/env python2 
# inspired by below 
# https://www.tutorialspoint.com/python/tk_canvas.htm

import Tkinter
top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="blue", height=300, width=300)

coord = 10 , 10 , 300 , 300 

arc = C.create_arc(coord , start = 0, extent = 359.9 , fill = "green")
C.pack()
top.mainloop()
