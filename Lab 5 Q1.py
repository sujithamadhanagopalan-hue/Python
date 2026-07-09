name = input("Enter your full name: ")
email = input("Enter your school email: ")
print("\nUppercase :", name.upper())
print("Lowercase :", name.lower())
print("Title Case:", name.title())

count = len(name.replace(" ", ""))
print("Characters (without spaces):", count)

if "@" in email and "." in email:
    username, domain = email.split("@")
    print("\nValid Email")
    print("Username:", username)
    print("Domain:", domain)
else:
    print("\nInvalid Email")
