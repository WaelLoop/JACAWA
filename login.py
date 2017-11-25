import cgi
print "Content-Type: text/html\n\n"
form = cgi.FieldStorage()
user= form.getvalue("username")
password= form.getvalue("password")
if user = "Jacawa@mail.mcgill.ca" and password = "abc123":
    print "success"
else:
    print"INCORRECT PASSWORD"
