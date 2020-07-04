#! /usr/bin/env python2

# where are bugs ?
i = raw_input("pleae input values of i : ")
j = raw_input("pleae input values of j : ")

#if (cmp(i,j) == -1):
if (comp(i,j) == -1):
	print " j is bigger than i , i and j are " ,  i , j
#elif(cmp(i,j) == 1):
elif(comp(i,j) == 1):
	print " i is bigger than j , i and j are " ,  i , j
else:
	print " i and  j  are same , i and j are " ,  i , j
	
