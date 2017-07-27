from openpyxl import load_workbook

wb = load_workbook("xSL_test.xlsx")

print(wb.get_sheet_names())