#!/usr/bin/python
# -*- coding: utf-8 -*-

# First basic build to read data from Arduino COM port
# We also try to write to csv now

# Initialize
from __future__ import division
import serial
#import sys
import time
#import csv
import json
from saveCSV import WriteToCSV # Custom script for saving CSV

# Useful variables
mcuFreq = 50 # Microcontroller frequency, in Hz
mcuPeriod = 1 / mcuFreq # Python loop timing, in seconds

# Make serial connection
serial = serial.Serial("COM3", 115200, timeout=0)
if serial:
	print('connected')

databuffer = []

# Run the loop until it crashes
while True:
# for i in range(0,10):connected
	data = serial.readline().strip('\n\r')
	# if data:
		# print('Reading')
	# data = serial.readline().strip('\n\r')
 
	if len(data) > 0: # We only continue if we retrieve a line of data
		
		# Next we should determine if we receive a complete line of data.
		# Method one: Verify that string starts and ends with {}
		# Method two: verify a specific line length if we know what we're expecting
#		print(data)

		if data[0]=='{' and data[-1] == '}':
	 		print('Complete string')
#			print(data)
			
			try:
 				j = json.loads(data) # Putting this within a try loop is an easy way to reject the mashed data JSON strings that crash the loops
				

				if j:
#					print(j)
					# databuffer.append(j) # Add to a buffer
					# print(len(databuffer))
					csv_success = WriteToCSV(j) # Write to a CSV file
					print (csv_success)
			except:
				# This happens if the json file is formatted properly.
				# print(data)
				print('bad values')
				# break # Break is discouraged because it will crash the whole script
 			print ('\n')
	 		# time.sleep(.5)
	 	
 	
	time.sleep(mcuPeriod) # Wait some time before reading again

# json test
# data = '{"sensor":"gps","time":1351824120,"data":[48.756080,2.302038]}'
# if data[0] == '{' and data[-1] == '}':
# 	print 'String properly formatted'
# 	j = json.loads(data)
# 	print(data)
# 	print 'sensor is',j['sensor']
# 	print 'data is', j['data'] 
# 	print json.dumps(j, indent=4) # Pretty print the data