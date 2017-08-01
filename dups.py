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
import re
from sheetInfo import headers, column_number
from sheetData import get_sheetdata
import time 

startTime = time.time()

data = get_sheetdata("dataset/uspDataset_test.xlsx")

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

outsheet_full = buk.active
outsheet_full.title = 'usp total'

# create sheet for 1 usp
uspOne = buk.create_sheet('usp dups')

# re.compile(r'<p>(.*?)</p>')
