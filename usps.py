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
import sys
sys.path.append('C:\\Code\\uspChecks\\library')
from sheetInfo import headers, column_number
from sheetData import get_sheetdata

data = get_sheetdata("dataset/uspDataset_current.xlsx")

# for row in data.iter_rows('A{}:A{}'.format(2, 10)):
# 	for cell in row:
# 		print(cell.value)

# get column by header

# provide options for standard input based on headers dict

headers = headers(data)
input1 = sys.argv[1]
column_one = headers[input1]
col_num_one = column_number(column_one)
input2 = sys.argv[2]
column_two = headers[input2]
col_num_two = column_number(column_two)

# number of rows
count = data.max_row

buk = Workbook()

outsheet = buk.active

# name the output headers
# make this dynamic
outsheet.cell(row=1, column=1, value=input1)
outsheet.cell(row=1, column=2, value=input2)

for n in range(2, 5):
	outsheet.cell(row=n, column=1, value=(data.cell(row=n, column=col_num_one).value))
	outsheet.cell(row=n, column=2, value=(data.cell(row=n, column=col_num_two).value))

# data.cell(row=n, column=col_num_two).value)

buk.save('output.xlsx')