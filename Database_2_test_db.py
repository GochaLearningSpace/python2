#! /usr/bin/env python2 

import MySQLdb
# to create data base , please follow below steps.


# https://support.rackspace.com/how-to/install-mysql-server-on-the-ubuntu-operating-system/
db =  MySQLdb.connect("localhost" , "testuser" , "test123" , "TESTDB" )

cursor = db.cursor()

cursor.execute ("SELECT VERSION()")


data = cursor.fetchone()
print "Database version : %s " % data

db.close
