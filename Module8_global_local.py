#! /usr/bin/env python2

a = "one"
def my_func():
	b="two"
	huh_l = locals()
	huh_g = globals()
	c="three"
	huh_l['d']="four"
	huh_g['d']="four"
	print "huh_l is : " , huh_l
	print "huh_g is : " , huh_g

my_func()
huh1_l = locals()
huh1_g = globals()

print "huh1_l is : " , huh1_l
print "huh1_g is : " , huh1_g

print "cmp(huh1_l, huh1_g) : " , cmp(huh1_l, huh1_g)
