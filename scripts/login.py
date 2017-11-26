import cgi
print "Content-Type: text/html\n\n"
form = cgi.FieldStorage()
user= form.getvalue("username")
password= form.getvalue("password")
if user == "Jacawa@mail.mcgill.ca" and password == "abc123":
    print( '<html>')
    print( '<head></head>')
    print( '<body>')
    print( '<h2>SUCCESS</h2>')
    print( '</body></html>')
else:
    print( '<html>')
    print( '<head></head>')
    print( '<body>')
    print( '<h2>INCORRECT LOGIN</h2>')
    print( '</body></html>')
