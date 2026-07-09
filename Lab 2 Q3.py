# Online Shopping Checkout System

print("ONLINE SHOPPING CHECKOUT")

customer_name=input("Enter customer name: ")
price1=float(input("Enter price of Product 1: "))
quantity1=int(input("Enter quantity of Product 1: "))

price2=float(input("Enter price of Product 2: "))
quantity2=int(input("Enter quantity of Product 2: "))

price3=float(input("Enter price of Product 3: "))
quantity3=int(input("Enter quantity of Product 3: "))

is_member=input("Are you a member? (yes/no):")
if is_member=="yes":
    print("member")
else:
    print("not a member")
coupon_eligibility=input("Do you have a valid coupon? (yes/no): ")
if coupon_eligibility=="yes":
    print("eligible for coupon")
else:
    print("not eligible for coupon")

payment_method=input("Enter payment method (UPI/Card/NetBanking/COD):")

subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)

# Tiered Discount
if subtotal>=10000:
    discount_rate=0.30
elif subtotal>=5000:
    discount_rate=0.20
elif subtotal>=2000:
    discount_rate=0.10
else:
    discount_rate=0.05

tiered_discount=subtotal*discount_rate

member_discount=subtotal*0.05 if is_member else 0

# Coupon Discount
coupon_discount = subtotal*0.08 if coupon_eligibility else 0

# Total Discount
total_discount=tiered_discount+member_discount+coupon_discount

discounted_amount=subtotal-total_discount

reward_points=int(discounted_amount // 100)

if is_member:
    reward_points*= 2

# Reward Value (Rs.1 per 10 points)
reward_value=reward_points//10

tax=discounted_amount*0.18

if discounted_amount>=5000:
    shipping=0
elif discounted_amount>=2000:
    shipping=50
else:
    shipping=100

cod_charge=40 if payment_method=="cod" else 0
final_amount = (discounted_amount+tax+shipping+cod_charge- reward_value)

premium_upgrade=(discounted_amount>=15000 or reward_points>= 500)


print("SHOPPING BILL")
print("Customer name:", customer_name)

print("Purchase Summary")
print("Subtotal: Rs.",subtotal)

print("Discounts")
print("Tiered Discount: Rs.", tiered_discount)
print("Member Discount: Rs.", member_discount)
print("Coupon Discount: Rs.", coupon_discount)
print("Total Discount:  Rs.", total_discount)

print("Charges")
print("Amount After Discount: Rs.", discounted_amount)
print("GST (18%): Rs.",tax)
print("Shipping Charge: Rs.",shipping)
print("COD Charge: Rs.",cod_charge)

print("Loyalty Rewards")
print("Reward Points Earned:",reward_points)
print("Reward Value Used:Rs.",reward_value)

print("Final Amount Payable: Rs.", final_amount)

if premium_upgrade:
    print("Congratulations! You are eligible for a Premium Membership Upgrade.")
else:
    print("Premium Membership Upgrade: Not Eligible")

