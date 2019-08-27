# This file generate code with combination of number concat to txt
# Edit records for amount of records
# Edit stringLength for the random Length

import random
import string
import csv

records=50000

def randomDigits(stringLength=15):
    """Generate a random string of digits """
    password_characters = string.digits
    return ''.join(random.choice(password_characters) for i in range(stringLength))

fieldnames=['code']
writer = csv.DictWriter(open("txtconcatnum.csv", "w"), fieldnames=fieldnames)

code = randomDigits()

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('code', 'MAJ'+randomDigits(15))]))