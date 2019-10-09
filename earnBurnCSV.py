# This file generate for earn and burn page as csv file for bulk upload
# Edit records for amount of records
# Edit studentCode for studentcode
# Edit randint for range of point in line 26

import random
import string
import csv

from random import seed
from random import randint

records=5

userCode = "b521012345","b521012346","b521012347","b521012348","b521012349","b521012350","b521012351","b521012352","b521012353","b521012354"

actionType = "EARN","BURN"

fieldnames=['STUDENT CODE','ACTION','POINT']
writer = csv.DictWriter(open("randomEarnBurn.csv", "w"), fieldnames=fieldnames)

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(1,records+1):
	studentCode = random.choice(userCode)
	action = random.choice(actionType)
	value = randint(1,10)
  	writer.writerow(dict([
    ('STUDENT CODE', studentCode),('ACTION', action),('POINT', value)]))