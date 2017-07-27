from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

import string

wb = load_workbook("dataset/uspDataset_current.xlsx")

names = wb.get_sheet_names()

data = wb[names[0]]

counter = 0
for cell in next(data.rows):
	counter += 1
	if cell.value is not None:	
		print(get_column_letter(counter))		
		print(cell.value)
		print("\n")

