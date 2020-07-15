#! /usr/bin/env python2
print "input file name: "
file_name = raw_input()
fo = open(file_name, "rb")
print "Name of the file : " , fo.name
#readed_txt=fo.read(10)
readed_txt=fo.read(100)
print(readed_txt)
fo.close()
