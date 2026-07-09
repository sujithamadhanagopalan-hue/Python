s="abc"
s1="abc"
print(s)
print(s1)
print(4*s1)
"Table"=='chair'
"Table"=="table"
print(4*'ab')
print("b" in 'abc')
print("bc" in 'abc')
print("cb" not in 'abc')
print("a" not in 'abc')
#take the str as user input and check the length of it.
s=input("enter a string")
print(len(s))
print(s[0])
print(s[len(s)-1])
print(s[0:(len(s)-1)])
print(s[1:(len(s)-2)])
print(s[0:len(s)])
print(s[-1:])
print(s[-1: len(s)-1])
print(s[-1:len(s)])
print(s[-1:0])
print(s[::-1])
name="sujitha"
for a in name:
    print(a)
for i in range(len(name)):
    print(str(i) +""+ name[i])
#take a name as user input, and print it with a greeting.
name=input("enter your name")
print("good morning",name)
i=1
while True:
    if i%3==0:
        break
    print(i,end='')
    i=i+1
    
