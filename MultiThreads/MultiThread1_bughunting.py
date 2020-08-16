# Created by Gocha, inspired by https://www.tutorialspoint.com/python/python_multithreading.htm
#!/usr/bin/env python2

import time
import thread

# Defining functions to print current time by using thread name and delay
def print_current_time(threadName, delay):
	count = 0 
	while count < 5:
		time.sleep(delay)
		count += 1
		print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create 4 threads as follows
try:
	thread.start_new_thread( print_current_time, ("Thread-1", 2, ) )
	thread.start_new_thread( print_current_time, ("Thread-2", 4, ) )
	thread.start_new_thread( print_current_time, ("Thread-3", 3, ) )
	thread.start_new_thread( print_current_time, ("Thread-4", 1, ) )
except:
	print "Error : start_new_thread failed"

while True:
	pass
 

