def addNewEntry(id, dob, firstName, lastName, location ,healthStatus):
    if int(id[:2]) < 20:
        filename = '../data/20'+id[:2]+".csv"
    else:
        filename = '../data/19'+id[:2]+".csv"
    f = open(filename, "a+")
    f.write(id + ", " + dob + ", "+firstName + ", "+ lastName + ", " + location + ", " + healthStatus +"\n")
    f.close()
    return
