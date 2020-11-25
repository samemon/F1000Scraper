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
# importing module to parse xml
import lxml.etree as ET
# importing module for directory creation
import os
# importing module for packaging
import sys


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

	Returns: query: string
	"""

	query = 'https://f1000research.com/extapi/search?q='
	if(keyword):
		query = query + 'R_TI:"'+keyword+'" AND '
	
	query = query + 'R_PUD:['+str(date_from_ms)+' TO '+\
		str(date_to_ms)+']'

	return query


def get_all_dois(url, dois, number_of_pages):
	"""
	This function takes in url query, dois list 
	and number of pages, and crawls through all 
	the pages and collects all dois.

	Input:
		- query: url string
		- dois: list
		- number of pages (integer > 1)
	
	Output: nothing

	Actions:
		- Appends to the dois list 
	"""

	for page in range(2, number_of_pages):
		url_with_page = url[:] + "&page=" + str(page)

		# opening the url and scraping
		opener = urllib.request.build_opener()
		tree = ET.parse(opener.open(url_with_page))

		for p in tree.xpath("//results//doi"):
			dois.append(p.text.strip())


	
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
	url  = requests.get(query).url

	'''
	# Now that we have a query, we need to wget
	
	html = ""
	with urllib.request.urlopen(url.url) as f:
		html = f.read().decode('utf-8')
	'''

	"""
	Now that we have the xml, we need to parse it, 
	get two things: (i) number of pages, and (ii) 
	all the dois as list.
	"""

	# opening the url and scraping
	opener = urllib.request.build_opener()
	tree = ET.parse(opener.open(url))

	# parsing the xml
	
	number_of_pages = int(tree.xpath('//@totalNumberOfPages')[0])

	# initializing a list of dois
	dois = []


	# extract all dois
	for p in tree.xpath("//results//doi"):
		dois.append(p.text.strip())

	
	# now we get all dois from all pages
	get_all_dois(url, dois, number_of_pages)
	
	# now that we have all dois, let get their xmls/pdfs
	base = 'https://f1000research.com/extapi/article/'
	if(output_format == "xml"):
		base = base + 'xml?doi='
	elif(output_format == "pdf"):
		base = base + 'pdf?doi='
	else:
		raise("Format not supposed")

	# lets check if the output directory exists else create
	if not os.path.exists(output_directory):
		os.makedirs(output_directory)

	print("Number of files downloading:", len(set(dois)))
   	# reading and writing xml
	for doi in dois[300:]:
		try:
			doi_query = base + doi
			print("Doi:",doi)
			opener = urllib.request.build_opener()
			url_open = opener.open(doi_query)
			xml = open(output_directory+"/"+doi.split("/f1000research.")[1]+\
					".xml", "w+")
			xml.write(url_open.read().decode('utf-8'))
			xml.close()
		except:
			print("COULD NOT DOWNLOAD:",doi)

	print("Downloaded",len(dois),"files.")
	return


if __name__ == "__main__":
	argv = sys.argv[1:]
	if(len(argv) < 4 or len(argv)> 5):
		print("Usage: python3 scrape.py <date from as dd-mm-yyyy> or '*'' "\
			"<date to as dd-mm-yyyy or '*'> <output_directory_path> "\
			"<output_format as 'xml' or 'pdf' <keyword (optional>")
		sys.exit()
	else:
		date_from = argv[0]
		date_to = argv[1]
		output_directory = argv[2]
		output_format = argv[3]

		if(len(argv) == 4):
			download(date_from, date_to, output_directory,output_format)
		else:
			download(date_from, date_to, output_directory,
					output_format, argv[4])


# Testing date conversion to ms
#download("1-1-2018","1-1-2020", "/Users/samemon/desktop/nyuad/F1000Scraper/api/data","xml")



