#!/usr/bin/env python
#File IO program
import csv
import cgi
def IDgenerator(dob, fname, lname):
    
    dob = dob.split("/")
    
    dob[0] = dob[0][2:]
    
    fname = list(fname)
    lname = list(lname)
    
    
    
    ID = dob[2] + dob[1] + dob[0] + str(ord(fname[0])-97) + str(ord(fname[1])-97) + str(ord(fname[2])-97) + str(ord(lname[0])-97) + str(ord(lname[1])-97) + str(ord(lname[2])-97)
    
    return ID

form = cgi.FieldStorage()
dob = form["DOB"].value
year = dob.split("/")[0]
fname = form["fname"].value
lname = form["lname"].value
print "Content-Type:text/html\n\n"
ID = IDgenerator(dob,fname,lname)
#Counter is used to keep track of correct row.
counter = 1
#Variable to track position.
position = None
#Accumulator
x = "ID Not Found."
file_name = year + ".csv"
#Reads through the csv file to find the refugee.
with open (file_name,'rb') as myDb:
    reader = csv.reader(myDb, delimiter = ',')
    for row in reader:
        if ID == row[0]:
            x = row
                position = counter
        counter = counter + 1
myDb.close()
if x == 'ID Not Found.':
    error_page = """<!DOCTYPE html>
        <html lang="en" >
        <head>
        <meta charset="UTF-8">
        <title>Search Form</title>
        <link href='https://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
        <link rel="stylesheet" href="../css/style.css">
        
        </head>
        
        <body>
        <div class="form">
        
        <div class="tab-content">
        <div id="search">
        <h1>Refugee Not Found</h1>
        <form action="search.py" method="post">
        
        <div class="top-row">
        <div class="field-wrap">
        <label>
        First Name<span class="req">*</span>
        </label>
        <input type="text" name="fname" required autocomplete="off" />
        </div>
        
        <div class="field-wrap">
        <label>
        Last Name<span class="req">*</span>
        </label>
        <input type="text" name="lname" required autocomplete="off"/>
        </div>
        </div>
        
        <div class="bottom-row">
        <div class="field-wrap">
        <label>
        DOB (yyyy/mm/dd)<span class="req">*</span>
        </label>
        <input type="DOB" name="DOB" required autocomplete="off"/>
        </div>
        </div>
        
        <button type="submit" class="button button-block"/>Search</button><br>
        </form>
        <form action="../new_refugee.html" method="post">
        <button type="submit" class="button button-block"/>New Entry</button><br>
        </form>
        
        
        </form>
        
        </div>
        
        <div id="login">
        </div>
        
        </div><!-- tab-content -->
        </div> <!-- /form -->
        <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
        
        <script  src="../js/index.js"></script>
        </body>
        </html> """
    print error_page
else:
    print x
