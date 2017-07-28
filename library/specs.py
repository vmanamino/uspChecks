# get info about the excel file

def headers(data):
	# need to modify to check for blank worksheets workbooks
	cols = {}
	for cell in next(data.rows):	
		if cell.value is not None:			
			cols[cell.column] = cell.value
	return cols