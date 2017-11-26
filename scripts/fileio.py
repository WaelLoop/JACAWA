#!/usr/bin/python
#File IO program 
import csv

ID = raw_input("Enter an ID:")

counter = 1
position = None
x = "ID Not Found."

with open ("refugeedb.csv",'rb') as myDb:
    reader = csv.reader(myDb, delimiter = ',')
    for row in reader:
       if ID == row[0]:
           x = row
           position = counter
          
    counter = counter + 1
#print x 
print position
if x != "ID Not Found.":
    print x


   
