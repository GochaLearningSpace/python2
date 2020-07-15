#! /usr/bin/env python2
print "input file name: "
file_name = raw_input()
fo = open(file_name, "rb")
print "Name of the file : " , fo.name
readed_txt=fo.read(10)
print "Reading string is : " , readed_txt

position = fo.tell()
print "Current file position : ", position

print "# reset file position : "
position = fo.seek(0,0)

position = fo.tell()
print "Current file position : ", position

readed_txt=fo.read(100)
print "Reading string is : " , readed_txt
position = fo.tell()
print "Current file position : ", position
fo.close()
