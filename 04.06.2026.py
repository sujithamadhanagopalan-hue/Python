c=float (input("enter the value of c")) #Conversion - centigrade to fahrenheit
f=((9*c)/5)+32
print (f) 

#Take the input in hour and convert it to minute and second

h=float(input("enter the value of h"))
m=h*60
print ("time in minutes", m)

s=m*60
print ("time in seconds",s)

#Take the input as year and convert to days and months, hour and minutes.
y=float(input("enter the value of y"))
d=y*365
print ("year in number of days",d)
m=y*12
print ("year in months",m)
h=24*365*y
print ("year in hours",h)
m=24*365*60*y
print ("year in minutes",m)

#Take input for speed of a car, miles per hour and convert it to kmph, km per min and km per sec.

mph=float (input("enter the speed of car in miles per hour"))
kmph=1.609*mph
print (" speed in kmph", kmph)
kmpm=1.609*mph/60
print (" speed in kmpm", kmpm)
kmps=kmpm/60
print ("speed in kmps",kmps)
cmph=160934*mph
print ("speed in cmph", cmph)
cmpm=cmph/60
print ("speed in cmpm", cmpm)
cmps=cmpm/60
print ("speed in cmps", cmps)
