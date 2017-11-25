#This program will search the csv database for the said refugee. 
#This program will generate IDs for every new entry of a refugee in the database. 
import cgi

form = cgi.FieldStorage()

dob = form.getvalue("dob")
fname = form.getvalue("fname")
lname = form.getvalue("lname")

