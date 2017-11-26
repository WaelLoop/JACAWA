#!/usr/bin/env python
import cgi
form=cgi.FieldStorage()
us=form.getvalue("username")
pw=form.getvalue("password")
print "Content-Type: text/html\n\n"
if us == 'Jacawa@mail.mcgill.ca':
    if pw == 'abc123':
        print "hi"
else:
    print"<html><head><title>Incorrect</title><body><h1><center>Incorrect Password </center></h1></body></html>"
