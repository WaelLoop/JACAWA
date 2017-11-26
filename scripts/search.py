#!/usr/bin/python
#File IO program 
import csv

form = cgi.FieldStorage()

dob = form.getvalue("DOB")
year,month,day = dob.split("/")

print year
print month
print day

ID = dob
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


# Print relevant HTML pages.  
#    
'''if x != "ID Not Found." :
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
            <h1 color = red> INFORMATION NOT FOUND. PLEASE CREATE NEW ENTRY. </h1>
          <h1>Search for an Existing Refugee</h1>

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
        <form action="new.py" method="post">
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
</html>
"""
    print "Content-Type: text/html\n\n"
    print error_page
else:
        found_info_page = """<!DOCTYPE html>
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
          <h1 color = red> INFORMATION FOUND: PLEASE ENTER NEW STATUS</h1>

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
        <form action="new.py" method="post">
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
</html>
"""
    print "Content-Type: text/html\n\n"
    print found_info_page'''

   










   
