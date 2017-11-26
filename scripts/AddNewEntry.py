import cgi
import csv
import requests
import json
from idgen import IDgenerator

form = cgi.FieldStorage()

dob = form["DOB"].value
fName = form["fname"].value
lName = form["lname"].value
healthStatus = form["healthStatus"].value

id = IDgenerator(dob, fName, lName)

def addNewEntry(id, dob, fName, lName, healthStatus):
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    city = j['city']
    
    if int(id[:2]) < 20:
        filename = '../data/20'+id[:2]+".csv"
    else:
        filename = '../data/19'+id[:2]+".csv"
    f = open(filename, "a+")
    f.write(id + ", " + dob + ", "+fName + ", "+ lName + ", " + city + ", " + healthStatus +"\n")
    f.close()
    return
