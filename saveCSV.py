# Functions for saving to CSV

import time
from os.path import exists
import csv

def WriteToCSV(datalist):
	""" This function accepts data and writes to CSV file. 
	A better optimization on this CSV script for the future would be for the CSV write to recognize the JSON hierarchy and 
	write the CSV according to JSON structure.
	"""

	global csv_success
	# Define header
	header = ['time', 'accx', 'accy', 'accz', 'gx', 'gy', 'gz', 'mx', 'my', 'mz']

	# Define our file
	filename = str(time.strftime("%y_%m_%d_") + "log.csv")

	# Handling to open our file if it exists or create new one
	if exists(filename):
		# try: 
		f = csv.writer(open(filename,"a"),lineterminator='\n')
			# break
		# except:
	else:
		f = csv.writer(open(filename,"a+"),lineterminator='\n')
		# Write our header line out if this is a new file
		f.writerow(header)
		


	
	f.writerow([ datalist['time'],datalist['acc'][0],datalist['acc'][1],datalist['acc'][2],datalist['gyro'][0],datalist['gyro'][1],datalist['gyro'][2],datalist['mag'][0],datalist['mag'][1],datalist['mag'][2] ])

	
	csv_success = True
	return csv_success
