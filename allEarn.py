# This file generate for earn and burn page as csv file for bulk upload
# Edit records for amount of records
# Edit studentCode for studentcode
# Edit randint for range of point in line 25

import random
import string
import csv

from random import seed
from random import randint

records=5

studentCode = 'b521012347'

actionType = 'EARN','BURN'

fieldnames=['STUDENT CODE','ACTION','POINT']
writer = csv.DictWriter(open("randomEarnBurn.csv", "w"), fieldnames=fieldnames)

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(1,records+1):
	action = random.choice(actionType)
	value = randint(1,10)
  	writer.writerow(dict([
    ('STUDENT CODE', studentCode),('ACTION', action),('POINT', value)]))