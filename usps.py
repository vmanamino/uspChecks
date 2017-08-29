'''
Here present command line options
usp marketing, or usp editorial

then ask for input

present options asking all titles with one usp

all titles with duplicate usps

generate report with total number of titles with each option

later create report of each title that has option

'''

# https://stackoverflow.com/questions/38619471/iterate-through-all-rows-in-specific-column-openpyxl
from openpyxl.utils import coordinate_from_string, column_index_from_string
from openpyxl import Workbook
import os
import sys
sys.path.append('C:\\Code\\uspChecks\\library')
import re
from usp_parser import uspHtmlParser
# from html_tags import tag_content
from sheet_info import headers, column_number
from sheet_data import get_sheetdata
import time 

startTime = time.time()

data = get_sheetdata("dataset/uspDataset_current.xlsx")

# for row in data.iter_rows('A{}:A{}'.format(2, 10)):
# 	for cell in row:
# 		print(cell.value)


# cmd line input: this file [0] 'title' [1] usp field [2]
# get output file name from input

file = sys.argv[0]
file_parts = os.path.splitext(file)
file_stem = file_parts[0]

# provide options for standard input based on headers dict

headers = headers(data)
input1 = sys.argv[1]
column_in_one = headers[input1]
col_num_in_one = column_number(column_in_one)
input2 = sys.argv[2]
column_in_two = headers[input2]
col_num_in_two = column_number(column_in_two)
isbn = headers['isbn']
isbn_col = column_number(isbn)
prod_cat = headers['product_category']
prod_cat_col = column_number(prod_cat)
market_us = headers['marketing_class_us']
market_us_col = column_number(market_us)
market_row = headers['marketing_class_row']
market_row_col = column_number(market_row)
market_dach = headers['marketing_class_dach']
market_dach_col = column_number(market_dach)



# number of rows
count = data.max_row

buk = Workbook()

overview = buk.active
overview.title = 'usp html'

# create sheet for 1 usp
usp_input2 = buk.create_sheet(input2)

# name the output headers
# make this dynamic
n_row_overview = 1
overview.cell(row=n_row_overview, column=1, value=input1)
overview.cell(row=n_row_overview, column=2, value="ISBN")
overview.cell(row=n_row_overview, column=3, value=input2)
overview.cell(row=n_row_overview, column=4, value="# HTML Tags")
overview.cell(row=n_row_overview, column=5, value="Product Category")
overview.cell(row=n_row_overview, column=6, value="Marketing US")
overview.cell(row=n_row_overview, column=7, value="Marketing ROW")
overview.cell(row=n_row_overview, column=8, value="Marketing DACH")



# 1 usp sheet
n_row_input2 = 1
usp_input2.cell(row=n_row_input2, column=1, value=input1)
usp_input2.cell(row=n_row_input2, column=2, value="ISBN")
usp_input2.cell(row=n_row_input2, column=3, value=input2)
usp_input2.cell(row=n_row_input2, column=4, value="# of HTML tags")
usp_input2.cell(row=n_row_input2, column=5, value="# of HTML-USPs")
usp_input2.cell(row=n_row_input2, column=6, value="USP content")


for n in range(2, count):
	project_prelim = data.cell(row=n, column=16).value
	p = re.compile(r'\bpreliminary\b')
	if not p.search(project_prelim):
		parser = uspHtmlParser()
		n_row_overview += 1
		inOne = data.cell(row=n, column=col_num_in_one).value
		inTwo = data.cell(row=n, column=col_num_in_two).value		
		parser.feed(inTwo)
		html_total = len(parser.tags)
		overview.cell(row=n_row_overview, column=1, value=inOne)
		overview.cell(row=n_row_overview, column=2, value=data.cell(row=n, 
			column=isbn_col).value) # ISBN
		overview.cell(row=n_row_overview, column=3, value=inTwo)
		overview.cell(row=n_row_overview, column=4, 
			value=html_total)
		overview.cell(row=n_row_overview, column=5, value=data.cell(row=n, 
			column=9).value)
		overview.cell(row=n_row_overview, column=6, value=data.cell(row=n, 
			column=market_us_col).value)
		overview.cell(row=n_row_overview, column=7, value=data.cell(row=n, 
			column=market_row_col).value)
		overview.cell(row=n_row_overview, column=8, value=data.cell(row=n, 
			column=market_dach_col).value)

		
		if html_total >= 1:
			n_usps = len(parser.output)
			n_row_input2 += 1
			usp_input2.cell(row=n_row_input2, column=1, value=inOne)
			usp_input2.cell(row=n_row_input2, column=2, value=data.cell(row=n,
				column=isbn_col).value) # ISBN
			usp_input2.cell(row=n_row_input2, column=3, value=inTwo)
			usp_input2.cell(row=n_row_input2, column=4, value=html_total)
			usp_input2.cell(row=n_row_input2, column=5, value=n_usps)
			usp_content = parser.usps_parsed()
			usp_input2.cell(row=n_row_input2, column=6, value=usp_content)
			

print_date = time.strftime("%d%m%y")
print_time = time.strftime("%I%M%S")

buk.save('results/'+file_stem+'_'+input2+'_'+print_date+'_'+print_time+'.xlsx')

print ('The script took {0} seconds !'.format(time.time() - startTime))