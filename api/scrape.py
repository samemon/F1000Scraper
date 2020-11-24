#!/usr/bin/env python

"""
This api will be used to scrape data 
from the F10000Research site. It 
is a wrapper around the already 
existent api.
"""

__author__ = "Shahan Ali Memon"
__copyright__ = "Copyright 2021, NYUAD"
__credits__ = "Bedoor AlShebli"
__version__ = "1.0.0"
__maintainer__ = "Shahan Ali Memon"
__email__ = "shahan@nyu.edu"

# Importing module needed for converting date to ms
import datetime


def convert_date_to_ms(d):
	"""
	This function takes in a date 
	of the format "dd-mm-yyyy" (string)
	and converts it to milliseconds in relation 
	to the unix epoch time
	"""

	# Splitting to get day, month, year
	dd,mm,yyyy = list(map(lambda e: int(e), d.split("-")))
	# Getting the date object
	date_obj = datetime.datetime(yyyy, mm, dd)
	# Getting the epoch time
	epoch = datetime.datetime.utcfromtimestamp(0)
	# Converting to ms and return
	return int((date_obj - epoch).total_seconds() * 1000.0)



def download(date_from, date_to, output_directory,
		output_format, keyword=None):

	"""
	This function takes in date_from, date_to, 
	output directory path, output_format and 
	an optional keyword argument and downloads 
	the papers from F1000Research published 
	from date_from to date_to in an XML format 
	(that contain an optional keyword if provided) 
	in the output directory. 

	Input: 
		- date_from: string in the format dd-mm-yyyy
		- date_in: string in the formmat dd-mm-yyyy
		- output_directory: absolute path to the directory
		- output_format: string ("xml" or "pdf")
		- keyword: optional string

	Output:
		- Does not return anything.

	Action:
		- Saves the papers in an XML format to the 
		output directory. 
		- Prints the number of papers downloaded.
	"""
	
	"Let us first parse the date arguments"


	"First we need to convert the dates to milliseconds"
	date_from_ms = convert_date_to_ms(date_from)
	date_to_ms = convert_date_to_ms(date_to)

	print(date_from_ms)

	return

# Testing date conversion to ms
download("1-1-2020","1-1-2019", "","")



