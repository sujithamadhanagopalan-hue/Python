x={1:'A',2:'B',3:'C'}
print(x)

x={}
n=int(input('how many entries:'))
for i in range(n):
    key=int(input("enter the key value"))
    value=input('enter the value')
    x[key]=value
print("Dictionary:", x)

                

x={}
n=int(input('number of students'))
for i in range(n):
    key=str(input("enter register number"))
    value=float(input('enter attendance percentage'))
    x[key]=value
print("Dictionary:", x)

x={}
List1=(3,5,6,8)
List2=('A','B','C','D')
for i in range (len(List1)):
    for j in range(len(List2)):
        if i==j:
            x[List1[i]==List2[j]]
print(x)                

#create a dictionary of students attendance
