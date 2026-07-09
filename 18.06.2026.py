n=7
for i in range (10,1,-1):
    for j in range (i):
        print("*", end="")
    print("\n")

rows = 5
for i in range(1, rows + 1):
    spaces = " "* (rows - i)
    stars = "*" * i
    print(spaces + stars)
    
for i in range(1, rows+1):
    spaces=" " *(i-1)
    stars="*" * (rows-i+1)
    print(spaces+stars)
