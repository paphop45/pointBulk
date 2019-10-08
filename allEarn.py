# This file generate for earn and burn page as csv file for bulk upload
# Edit records for amount of records

import random
import string
import csv

records=5
action = 'EARN'

fieldnames=['ACTION']
writer = csv.DictWriter(open("MockEarn.csv", "w"), fieldnames=fieldnames)

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(1,records+1):
  writer.writerow(dict([
    ('ACTION', action)]))