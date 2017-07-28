# get info about the excel file

def headers(data):
	'''need to modify to check for blank worksheets workbooks
	returns dict of column letters matched with first column cell, which contains
	the descriptive header'''

	'''the first column cell going across contains BFLUX fields
	intended for command line args where the user enters BLFUX field name
	which points to the correct column in the spreadsheet'''
	
	cols = {}
	for cell in next(data.rows):	
		if cell.value is not None:			
			cols[cell.value] = cell.column
	return cols