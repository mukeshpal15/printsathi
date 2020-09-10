from openpyxl.workbook import Workbook 

import pandas 
import xlsxwriter
def hello():
	mm='kkkkkkk.xlsx'
	workbook = xlsxwriter.Workbook(mm)
	worksheet = workbook.add_worksheet()

	# Some data we want to write to the worksheet.
	expenses = (
	    ['Rent', 345],
	    ['Gas',   45435],
	    ['Food',  345345],
	    ['Gym',    3453454],
	)

	# Start from the first cell. Rows and columns are zero indexed.
	row = 0
	col = 0

	# Iterate over the data and write it out row by row.
	for item, cost in (expenses):
	    worksheet.write(row, col,     item)
	    worksheet.write(row, col + 1, cost)
	    row += 1
	workbook.close()

	

	excel_data_df = pandas.read_excel(mm)

# print whole sheet data
	print(excel_data_df)
	return excel_data_df

