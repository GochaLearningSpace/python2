#! /usr/bin/env python2
import os
import shutil

#print os.environ['PATH']
src_file = "a.txt"
dst_file = "a_copy.txt"
org_file = "a_org.txt"

#bug# shutil.copy("org_file", "src_file")
shutil.copy(org_file, src_file)
os.rename(src_file, dst_file)

fo = open(dst_file, "rb")

print "Name of the file : " , fo.name
readed_txt=fo.read(100)
print "Reading string is : " , readed_txt

