def addNewEntry(iD, firstName, lastName, location ,healthStatus):
    f = open("refugeedb.csv", "a+")
    f.write("\n"+ iD + "," + firstName + ","+ lastName + "," + location + "," + healthStatus)
    f.close()
    return