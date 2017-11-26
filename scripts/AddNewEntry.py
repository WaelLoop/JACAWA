import cgi
import csv

form = cgi.FieldStorage()

dob = form["DOB"].value
fname = form["fname"].value
lname = form["lname"].value

def IDgenerator(dob, fname, lname):
    dob = dob.split("/")    
    dob[0] = dob[0][2:]
    fname = list(fname)
    lname = list(lname)
    ID = dob[2] + dob[1] + dob[0] + str(ord(fname[0])-97) + str(ord(fname[1])-97) + str(ord(fname[2])-97) + str(ord(lname[0])-97) + str(ord(lname[1])-97) + str(ord(lname[2])-97)  
    return ID

def addNewEntry(id, dob, firstName, lastName, location ,healthStatus):
    if int(id[:2]) < 20:
        filename = '../data/20'+id[:2]+".csv"
    else:
        filename = '../data/19'+id[:2]+".csv"
    f = open(filename, "a+")
    f.write(id + ", " + dob + ", "+firstName + ", "+ lastName + ", " + location + ", " + healthStatus +"\n")
    f.close()
    return

