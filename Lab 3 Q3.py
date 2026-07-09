#Develop a Python program that determines a
#customer's health insurance premium category based on age, BMI, smoking status,
#and pre-existing medical conditions.
#Use if and if-else statements to classify
#risk levels and calculate the applicable premium amount.


#Design a Python program for a citizen service portal where users select services such as passport renewal, driving
#license renewal, tax payment, utility bill payment, or grievance
#submission. Use match-case to route requests to the appropriate service workflow.
#Within each case, use nested if-elif-else statements to validate
#eligibility, calculate fees, apply discounts or penalties, and generate a
#final service summary.
# Select service: passport, license, tax, utility, grievance

service = input("enter your service")

match service:
    case "passport":
        age = int(input("enter your age"))
        has_passport = True 
        expired = True
        
        if has_passport:
            print("Must apply for a new passport")
        elif age < 16:
            print("Must renew in person.")
        else:
            fee = 130
            if expired:
                fee = fee + 60
            print("Passport Renewal Fee: Rs.", fee)

    case "license":
        points=int(input("enter your points"))
        expired_years = int(input("enter how many years before the licence got expired"))
        
        if points >=12:
            print("License suspended.")
        elif expired_years > 2:
            print("You must retake the driving test.")
        else:
            fee = 50
            if expired_years> 0:
                fee = fee + 25  
            print("License Renewal Fee: Rs.", fee)

    case "tax":
        income = 20000
        
        if income <= 15000:
            tax = income * 0.50
        elif income <= 46000:
            tax = income * 0.20
        else:
            tax = income * 0.30
        print("Total Tax Owed: Rs.", tax)

    case "utility":
        amount = int(input("enter amount to pay"))
        payment_method = "autopay"
        
        if amount <= 0:
            print("invalid amount.")
        else:
            if autopay:
                amount = amount - (amount * 0.10)  
            print("Bill Amount: Rs.", amount)

    case "grievance":
        message = input("enter your grievance")
        
        if message == "":
            print("Message cannot be empty.")
        elif len(message) < 20:
            print("Please provide more detail.")
        else:
            print("Grievance submitted successfully!")

    case _:
        print("Invalid Service Selected.")
