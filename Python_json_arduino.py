#!/usr/bin/python
# -*- coding: utf-8 -*-

# First basic build to read data from Arduino COM port
# We also try to write to csv now

# Initialize
import serial
import sys
import time
import csv
import json
from saveCSV import WriteToCSV # Custom script for saving CSV

# Useful variables
arduinotiming = 0.2 # Clock on arduino sketch, in seconds

# Make serial connection
serial = serial.Serial("COM3", 115200, timeout=0)
if serial:
	print('connected')

buffer = []

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
	 	# print(data)
	 	# print('start',data[0])
	 	# print('end',data[-1])
	 	if data[0]=='{' and data[-1] == '}':
	 		print('Complete string Detected')
			print(data)
			
	 		j = json.loads(data)
			buffer.append(j)

				
# 			csv_success = WriteToCSV(j)
# 			print csv_success
 			print ('\n')
	 		# time.sleep(.5)
	 	# print ('String begin and ends with',data[0],data[-1])
	 	# print ('length of data is',len(data))
 		# # if data[0] == '{' and data[-1] == '}': # Fact that this doesn't work tells me that something wrong with encoding
	 	
	 	# # print len(data)
	 	# j = json.loads(data)
	 	# print(data)
	 	
	 	# print(j)
	 	# print j['sensor']
	 	# print j['data']
 	
	time.sleep(0.010) # Wait some time before reading again

# json test
# data = '{"sensor":"gps","time":1351824120,"data":[48.756080,2.302038]}'
# if data[0] == '{' and data[-1] == '}':
# 	print 'String properly formatted'
# 	j = json.loads(data)
# 	print(data)
# 	print 'sensor is',j['sensor']
# 	print 'data is', j['data'] 
# 	print json.dumps(j, indent=4) # Pretty print the data