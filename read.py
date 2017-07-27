from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

wb = load_workbook("dataset/uspDataset_current.xlsx", read_only=True)

names = wb.get_sheet_names()

ws = wb[names[0]]

print(ws['A1'].value)


# print(names)

# wbR = Workbook()

# s1 = wbR.create_sheet(title="results")

# s1['A1'] = 'Header'

# row = 2

# col = 1

# for name in names:
# 	print(name)
# 	s1.cell(column=col, row=row, value=name)

# print(s1['A1'].value)

# wbR.save(filename="results/result.xlsx")

