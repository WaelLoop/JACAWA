#!/usr/bin/python
#File IO program: this program will try and match the ID formed by the user input to a record of a refugee.

import csv
import cgi

form = cgi.FieldStorage()

dob = form.getvalue("DOB")

ID = dob
print dob
#Counter is used to keep track of correct row.
counter = 1 
#Variable to track position.
position = None
#Accumulator
x = "ID Not Found."
#Reads through the csv file to find the refugee. 
with open ("../data/refugeedb.csv",'rb') as myDb:
    reader = csv.reader(myDb, delimiter = ',')
    for row in reader:
       if ID == row[0]:
           x = row
           position = counter         
    counter = counter + 1
myDb.close()











   
