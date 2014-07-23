import string
import re

outFile = open('allfilms.nt', 'w')

def writeToFile():
    global outFile
    count = 0

    for line in file('allfilms.tsv', 'r'):
        if count > 0:
            linearray = line.split('\t')
            filmID = linearray[0]
            title = linearray[1]

            outFile.write(filmID + " <http://purl.org/dc/terms/title> " +
                title + " .\n")
            
        count += 1

    count = 0

    for line in file('allfilms.tsv', 'r'):
        if count > 0:
            linearray = line.split('\t')
            filmID = linearray[0]
            actor = linearray[2]

            outFile.write(filmID + " <http://data.linkedmdb.org/resource/actor> " +
                actor + " .\n")
            
        count += 1

    count = 0

    for line in file('allfilms.tsv', 'r'):
        if count > 0:
            linearray = line.split('\t')
            filmID = linearray[0]
            director = linearray[3][:-2]

            outFile.write(filmID + " <http://data.linkedmdb.org/resource/director> " +
                director + "\" .\n")

            
        count += 1

writeToFile()
outFile.close();



