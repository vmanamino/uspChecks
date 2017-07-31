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
# from openpyxl import load_workbook
# from openpyxl import Workbook
# from openpyxl.compat import range
# from openpyxl.utils import get_column_letter
import sys
sys.path.append('C:\\Code\\uspChecks\\library')
from sheetInfo import headers
from sheetData import get_sheetdata

data = get_sheetdata("dataset/uspDataset_current.xlsx")

print(data.max_row)

