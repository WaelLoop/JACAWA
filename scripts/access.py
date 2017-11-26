#!/usr/bin/env python
import cgi
form=cgi.FieldStorage()
us=form.getvalue("username")
pw=form.getvalue("password")
print "Content-Type: text/html\n\n"
if us == 'Jacawa@mail.mcgill.ca':
        if pw == 'abc123':
                print '<!DOCTYPE html><html lang=\"en\" ><head><meta charset=\"UTF-8\"><title>Search Form</title><link href=\"https://fonts.googleapis.com/css?family=Titillium+Web:400,300,600\" rel=\"stylesheet\" type=\"text/css\"><link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css\"><link rel=\"stylesheet\" href=\"../css/style.css\"></head><body><div class=\"form\"><div class=\"tab-content\"><div id=\"search\"><h1>Search for an Existing Refugee</h1><form action=\"./search.py\" method=\"post\"><div class=\"top-row\"><div class=\"field-wrap\"><label>First Name<span class=\"req\">*</span></label><input type=\"text\" name=\"fname\" required autocomplete=\"off\" /></div><div class=\"field-wrap\"><label>Last Name<span class=\"req\">*</span></label><input type=\"text\" name=\"lname\" required autocomplete=\"off\"/></div></div><div class=\"bottom-row\"><div class=\"field-wrap\"><label>DOB (yyyy/mm/dd)<span class=\"req\">*</span></label><input type=\"DOB\" name=\"DOB\" required autocomplete=\"off\"/></div></div><button type=\"submit\" class=\"button button-block\"/>Search</button></form><form action=\"../new_refugee.html\" method=\"post\"><br><button type=\"submit\" class=\"button button-block\"/>New Entry</button><br></form></div><div id=\"login\"></div></div><!-- tab-content --></div> <!-- /form --><script src=\"http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js\"></script><script  src=\"../js/index.js\"></script></body></html>'
else:
        print"<html><head><title>Incorrect</title><body><h1><center>Incorrect Password </center></h1></body></html>"
