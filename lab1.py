import csv
import urllib

PopulationAndDensity = "http://boxnumbertwo.com/PittsburghData/Population_and_Density.csv"

fhand = urllib.urlopen(PopulationAndDensity)

pop1940 = dict()
pop1950 = dict()
pop1960 = dict()
pop1970 = dict()
pop1980 = dict()
pop1990 = dict()
pop2000 = dict()
pop2010 = dict()
try:
	reader = csv.reader(fhand)
	next(reader, None)  # skip the headers
	for row in reader:
		#print row[0]
		pop1940[row[0]] = int(row[2].replace(",",""))
		pop1950[row[0]] = int(row[3].replace(",",""))
		pop1960[row[0]] = int(row[4].replace(",",""))
		pop1970[row[0]] = int(row[5].replace(",",""))
		pop1980[row[0]] = int(row[6].replace(",",""))
		pop1990[row[0]] = int(row[7].replace(",",""))
		pop2000[row[0]] = int(row[8].replace(",",""))
		pop2010[row[0]] = int(row[9].replace(",",""))
		#print pop2010			
finally:
	fhand.close()

total = 0
for key in pop1940:
    total = total + pop1940[key]
pop1940["total"]=total
#print total

total = 0
for key in pop1950:
    total = total + pop1950[key]
pop1950["total"]=total
#print total

total = 0
for key in pop1960:
    total = total + pop1960[key]
pop1960["total"]=total
#print total

total = 0
for key in pop1970:
    total = total + pop1970[key]
pop1970["total"]=total
#print total

total = 0
for key in pop1980:
    total = total + pop1980[key]
pop1980["total"]=total
#print total

total = 0
for key in pop1990:
    total = total + pop1990[key]
pop1990["total"]=total
#print total

total = 0
for key in pop2000:
    total = total + pop2000[key]
pop2000["total"]=total
#print total

total = 0
for key in pop2010:
    total = total + pop2010[key]
pop2010["total"]=total
#print total

print "Difference between every decade:"
print "Difference between 1940-1950:", pop1950["total"]-pop1940["total"]
print "Difference between 1950-1960:", pop1960["total"]-pop1950["total"]
print "Difference between 1960-1970:", pop1970["total"]-pop1960["total"]
print "Difference between 1970-1980:", pop1980["total"]-pop1970["total"]
print "Difference between 1980-1990:", pop1990["total"]-pop1980["total"]
print "Difference between 1990-2000:", pop2000["total"]-pop1990["total"]
print "Difference between 2000-2010:", pop2010["total"]-pop2000["total"]

print "\nDifference between every decade for Mount Washington:"
print "Difference between 1940-1950:", pop1950["Mount Washington"]-pop1940["Mount Washington"]
print "Difference between 1950-1960:", pop1960["Mount Washington"]-pop1950["Mount Washington"]
print "Difference between 1960-1970:", pop1970["Mount Washington"]-pop1960["Mount Washington"]
print "Difference between 1970-1980:", pop1980["Mount Washington"]-pop1970["Mount Washington"]
print "Difference between 1980-1990:", pop1990["Mount Washington"]-pop1980["Mount Washington"]
print "Difference between 1990-2000:", pop2000["Mount Washington"]-pop1990["Mount Washington"]
print "Difference between 2000-2010:", pop2010["Mount Washington"]-pop2000["Mount Washington"]

print "\nDifference between every decade for North Oakland:"
print "Difference between 1940-1950:", pop1950["North Oakland"]-pop1940["North Oakland"]
print "Difference between 1950-1960:", pop1960["North Oakland"]-pop1950["North Oakland"]
print "Difference between 1960-1970:", pop1970["North Oakland"]-pop1960["North Oakland"]
print "Difference between 1970-1980:", pop1980["North Oakland"]-pop1970["North Oakland"]
print "Difference between 1980-1990:", pop1990["North Oakland"]-pop1980["North Oakland"]
print "Difference between 1990-2000:", pop2000["North Oakland"]-pop1990["North Oakland"]
print "Difference between 2000-2010:", pop2010["North Oakland"]-pop2000["North Oakland"]

print "\nDifference between every decade for Shadyside:"
print "Difference between 1940-1950:", pop1950["Shadyside"]-pop1940["Shadyside"]
print "Difference between 1950-1960:", pop1960["Shadyside"]-pop1950["Shadyside"]
print "Difference between 1960-1970:", pop1970["Shadyside"]-pop1960["Shadyside"]
print "Difference between 1970-1980:", pop1980["Shadyside"]-pop1970["Shadyside"]
print "Difference between 1980-1990:", pop1990["Shadyside"]-pop1980["Shadyside"]
print "Difference between 1990-2000:", pop2000["Shadyside"]-pop1990["Shadyside"]
print "Difference between 2000-2010:", pop2010["Shadyside"]-pop2000["Shadyside"]

totalDiff20101940 = dict()
totalDiff=0
pop2010.pop("total")  #delete the element pop2010["total": total]
pop1940.pop("total")

for key in pop2010:
    totalDiff=pop2010[key]-pop1940[key]  
    totalDiff20101940[key]=totalDiff
    #print totalDiff20101940
totalDiff20101940 = sorted(totalDiff20101940.items(),key=lambda x:x[1])  
#print totalDiff20101940  

print "\nDiffernce between different area from 1940 to 2010:"
print "\nTop-10 Worst Area"
for key in range(0,10):
    print "#", totalDiff20101940[key]

print "\nTop-10 Best Area"
for key in range(0,10):
    print "#", totalDiff20101940[len(totalDiff20101940)-1-key]
    
    


