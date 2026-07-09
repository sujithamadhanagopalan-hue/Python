#Developing a personalised smart water bottle.
#setting daily target for water intake based on age.
#take user inputs from user about water intake
#print personalised message according to their progress
#if target is achieved print congratulations
#if near target, then motivate and mention the amount left
#if very less insist on completing.

name=input("enter your name")
age=int(input("enter your age"))

if 5<=age<=10:
    goal = 1200 #in ml
elif 10<=age<=15:
    goal = 1600 #in ml
elif 15<=age<=20:
    goal = 2200
elif 20<=age<=60:
    goal = 3000
else:
    goal = 2000

print("hello", name)
intake=float(input("enter the amount of water intake"))

progress = (intake/goal)*100 #in percent
             
if progress == goal:
    print("congratulations you have met your hydration target")
elif progress <=0.7*goal:
    remaining=goal - intake
    print("You are almost there, keep hydrating")
    print (remaining, "ml is left")

else:
    remaining=goal - intake
    print ("meet your hydration goals, you need", remaining, "ml more")
    
print("name:",name)
print("age:",age)
print("intake:", intake)
print("progress:", progress)
