# This file generate code with combination of alphabet and number (upperlowermix)
# Edit records for amount of records
# Edit stringLength for the random Length

import random
import string
import csv

records=10000

def randomStringwithDigitsAndSymbols(stringLength=22):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(stringLength))

fieldnames=['code']
writer = csv.DictWriter(open("10krec22len.csv", "w"), fieldnames=fieldnames)

code = randomStringwithDigitsAndSymbols()

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('code', randomStringwithDigitsAndSymbols(18))]))