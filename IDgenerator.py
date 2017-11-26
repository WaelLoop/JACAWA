'''
Created on Nov 25, 2017

@author: ayoub
'''

def IDgenerator(dob, fname, lname):
    
    dob = dob.split("/")
        
    dob[2] = dob[2][2:]
    
    fname = list(fname)
    lname = list(lname)
    
    
    
    ID = dob[2] + dob[1] + dob[0] + str(ord(fname[0])-97) + str(ord(fname[1])-97) + str(ord(fname[2])-97) + str(ord(lname[0])-97) + str(ord(lname[1])-97) + str(ord(lname[2])-97)
        
    return ID
    
    
print(IDgenerator("02/08/1997", "ayoub", "elhanchi"))