a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
d=a+b*c
e=(a+b)*c
print(d)
print(e)

#check if a number lies withing the given range.
a=20
if 10<a<40:
    print("the number lies within the range")
else:
    print("the number is not in range")
a=10
b=5
c=10
print(a>b==c) #a>b is true and b==c is false, true and false becomes false

x=8
y=8
z=12
print(x==y<12)

a=15
b=10
c=5
print(a>b<c)

#&&=and
x=1
y=2
print(x and y)
#create a programme to authenticade username and password and give a message.
#a**=b gives a=a^b
#identity operators - is - true if operands are identical and is not- true is operands are not identical
#membership operator #in - True if value is found in the sequence and not in - True if the value is not found in the sequence.
#Ternary operator
#syntax:

a=10
b=5
print(a if a<b else b)
