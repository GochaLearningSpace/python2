#! /usr/bin/env python2

#KelvinToFahrenheit
def K2F(Temp):
	assert (Temp >= 0), "### Colder than absolute zero !"
	return ((Temp-273)*1.8)+32

print "#K2F(273) : ", K2F(273) 
print "#int(K2F(505.78)) : ", int(K2F(505.78) )
print "#K2F(-5) : ", K2F(-5) 
