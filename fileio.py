#File IO program 

import csv with open 

with open ("refugeedb.csv", newline='') as myDb:
    reader = csv.reader(myDb)
    for row in reader:
        print(row)