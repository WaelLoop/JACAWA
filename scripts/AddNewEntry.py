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

def addNewEntry(iD, firstName, lastName, location ,healthStatus):
    f = open("refugeedb.csv", "a+")
    f.write("\n"+ iD + "," + firstName + ","+ lastName + "," + location + "," + healthStatus)
    f.close()
    return

