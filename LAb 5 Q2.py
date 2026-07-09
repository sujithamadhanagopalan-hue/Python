password = input("Enter password: ")
sentence = input("Enter a sentence: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("\nStrong Password")
else:
    print("\nWeak Password")

sentence = sentence.lower()
words = sentence.split()

print("\nWord Frequency:")
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word in count:
    print(word, ":", count[word])
