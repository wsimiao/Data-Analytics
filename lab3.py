# -*- coding: utf-8 -*-
import re
import sqlite3 as lite
import os
import urllib
ratingWeb = "http://boxnumbertwo.com/MovieData/ratings.list"
f = urllib.urlopen(ratingWeb)
nameList = list()
element = []
newElement = []
for line in iter(f):
    line = re.sub(' +',' ',line.strip())   # line.strip:delete the char before and after the line
                                            # re.sub(' +', ' ') 把多个空格变成一个空格
                                            # line return as String
    line = line.split(" ", 3)               # line return as a list and line[0] as string
    nameAndDate = line[3].split(" {")
    nameAndDate = nameAndDate[0]    ##  "$100,000 Name That Tune" (1984) "$#*! My Dad Says" (2010) as String
    nameAndDate = nameAndDate.split("(")
    name = nameAndDate[0]  
    name = nameAndDate[0].replace('"','')
    name = name.replace("'",'"')
    #name = nameAndDate[0].split(" ",1)
    #name = name[1].replace("\"","")
    date = nameAndDate[1].replace(')','')
    print name + date
    #print type(date)  #### str
    #print name   ###   "#1 Single" 

    voteNum = int(line[1].replace("'",""))    ##voteNum: the amount of votes
    ratingNum = float(line[2].replace("'",""))  ## rating number
    element.append([name,date,voteNum,ratingNum])
    
print element[0][0]
for index in range(len(element)-1):
    if (element[index][0] == element[index+1][0]):
        if element[index][2]>element[index+1][2]:
            element[index+1] = element[index]
        else:
            element[index]= element[index+1]
#print element
for i in element:
    if i not in newElement:
        newElement.append(i)
print newElement  
print len(newElement)      
f.close()

con =None

##Create a folder for the database
directoryForDB = "/Users/simiao/Documents/Fall 2015/INFSCI 2725/ASSIGNMENT/Assignment 3/database/"## set directory 
if not os.path.exists(directoryForDB):
    os.makedirs(directoryForDB)
    
directoryForDB = directoryForDB + "movieRating.db"
con = lite.connect(directoryForDB)
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS movieList")
    cur.execute("CREATE TABLE movieList(movieName TEXT, movieDate TEXT, movieVote INT, movieRating REAL)")
    for index in range(len(newElement)):
        insertStatement= """INSERT INTO movieList VALUES ('%s','%s',%d,%f)""" % (newElement[index][0],newElement[index][1],newElement[index][2],newElement[index][3])
        cur.execute(insertStatement)
    con.commit
    
    

