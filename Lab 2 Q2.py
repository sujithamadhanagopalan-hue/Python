#Develop a Python program
#that calculates a household electricity bill using slab-based pricing.
#The program should apply different rates based on units consumed,
#add fixed charges and taxes, and
#determine whether the household qualifies for an energy-efficiency rebate.
#Use appropriate data types, nested expressions, and multiple
#operators to generate a detailed bill summary.

consumer_name=input("enter your name")
units=int(input("enter electricity consumption"))

if units<=100:
    charges=units*1.50
elif units<=200:
    charges=(100*1.50)+((units-100)*2.50)
elif units<=400:
    charges=(100*1.50)+(100*2.50)+((units-200)*4.00)
else:
    charges=(100*1.50)+(100*2.50)+(200*4.00)+((units-400)*6.5)
fixed_charge=100.0
total=charges+fixed_charge
tax=total*0.05
total_before_rebate=total+tax

if units<150:
    rebate=total_before_rebate*0.10
else:
    rebate=0.0
final_bill=total_before_rebate-rebate

#bill summary
print("Electricity bill")
print("consumer name:",consumer_name)
print("units consumed:", units, "kwh")
print("electricity charges: Rs.",charges)
print("fixed charge: Rs.", fixed_charge)
print("tax(5%):", tax)
print("Total Payable:",final_bill)

if rebate>0:
    print("Congratulations, you are eligible for rebate")
else:
    print("rebate not applicable")
    
