from openpyxl.workbook import Workbook 

import pandas as pd
import xlsxwriter

mm='kkkkkkk.xlsx'
workbook = xlsxwriter.Workbook("C://Users//Mukesh pal//Desktop/"+mm)
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



