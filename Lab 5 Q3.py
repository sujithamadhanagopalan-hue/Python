
message = input("Enter chat message: ")

message = " ".join(message.split())

message = message.replace(" u ", " you ")
message = message.replace(" r ", " are ")
message=message.replace("nd", "and")

words = message.split()

for i in range(len(words)):
    if words[i] == "u":
        words[i] = "you"
    elif words[i] == "r":
        words[i] = "are"
    elif words[i]=="nd":
        words[i]="and"

cleaned = " ".join(words)
encoded = ""

for ch in cleaned:
    if 'a' <= ch <= 'y':
        encoded += chr(ord(ch) + 1)
    elif ch == 'z':
        encoded += 'a'
    elif 'A' <= ch <= 'Y':
        encoded += chr(ord(ch) + 1)
    elif ch == 'Z':
        encoded += 'A'
    else:
        encoded += ch

print("\nCleaned Message:", cleaned)
print("Secret Message :", encoded)
