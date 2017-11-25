
import cgi

form = cgi.FieldStorage()

dob = form.getvalue("dob")
fname = form.getvalue("fname")
lname = form.getvalue("lname")

