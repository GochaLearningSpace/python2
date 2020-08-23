#! /usr/bin/env python2
# referring below site, but modified for this purpose.
# https://www.tutorialspoint.com/python/tk_radiobutton.htm

def select():
	selection = "Your selection is " + str(var.get())
	label.config(text = selection)

root = Tk()
var = IntVar
R1 = RadioButton ( root, text = "option 1", variable = var , value = 1, command=sel)
R2 = RadioButton ( root, text = "option 2", variable = var , value = 2, command=sel)
R3 = RadioButton ( root, text = "option 3", variable = var , value = 3, command=sel)

R1.pack(anchor = W)
R2.pack(anchor = W)
R3.pack(anchor = W)

label = Label(root)
label.pack()
root.mainloop()

