# This file generate for earn and burn page as XLSX file for bulk upload
# Edit records for amount of records
# Edit studentCode for studentcode

import random
import string
import xlsxwriter

from random import seed
from random import randint

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('randomEarnBurn.xlsx')
worksheet = workbook.add_worksheet()

i = 1
records = 5

userCode = "b521012345","b521012346","b521012347","b521012348","b521012349","b521012350","b521012351","b521012352","b521012353","b521012354"
studentCode = random.choice(userCode)

actionType = "EARN","BURN"
action = random.choice(actionType)

value = randint(1,10)

# Some data we want to write to the worksheet.
header = (
    ['STUDENT CODE', 'ACTION', 'POINT'],
)

data = (
	[studentCode, action, value],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for code, action, point in (header):
    worksheet.write(row, col,     code)
    worksheet.write(row, col + 1, action)
    worksheet.write(row, col + 2, point)
    row += 1

for i in range(1,records+1):
	studentCode = random.choice(userCode)
	action = random.choice(actionType)
	value = randint(1,10)
	worksheet.write(row, col,     studentCode)
	worksheet.write(row, col + 1, action)
	worksheet.write(row, col + 2, value)
	row += 1

workbook.close()