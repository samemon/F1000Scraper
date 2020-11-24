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
# importing module to wget
import urllib.request
import requests


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

def create_f1000_query(date_from_ms, date_to_ms, output_format, 
		keyword=None):

	"""
	This will create the query to get items from the F1000 
	page.
	
	Input: 
		- date_from_ms: int of date in ms
		- date_in: int of date in ms
		- output_format: string ("xml" or "pdf")
		- keyword: optional string for checking titles
	"""

	query = 'https://f1000research.com/extapi/search?q='
	if(keyword):
		query = query + 'R_TI:"'+keyword+'" AND '
	
	query = query + 'R_PUD:['+str(date_from_ms)+' TO '+\
		str(date_to_ms)+']'

	return query
	
def download(date_from, date_to, output_directory,
		output_format, keyword=None):

	"""
	This function takes in date_from, date_to, 
	output directory path, output_format and 
	an optional keyword argument and downloads 
	the papers from F1000Research published 
	from date_from to date_to in an XML format 
	(whose title contains the optional keyword if provided) 
	in the output directory. 

	Input: 
		- date_from: string in the format dd-mm-yyyy or *
		- date_in: string in the formmat dd-mm-yyyy or *
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


	#First we need to convert the dates to milliseconds
	date_from_ms = date_from
	date_to_ms = date_from

	if(date_from != "*"):
		date_from_ms = convert_date_to_ms(date_from)
	
	if(date_to != "*"):
		date_to_ms = convert_date_to_ms(date_to)

	# Now we need to form a query
	query = create_f1000_query(date_from_ms, 
			date_to_ms, 
			output_format)

	# Converting query to url object for control characters
	url  = requests.get(query)

	# Now that we have a query, we need to wget
	html = ""
	with urllib.request.urlopen(url.url) as f:
		html = f.read().decode('utf-8')
		print(html)

	return

# Testing date conversion to ms
download("1-1-2019","1-1-2020", "","")



