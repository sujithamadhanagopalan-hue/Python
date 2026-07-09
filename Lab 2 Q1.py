#Design a Python program for a monthly budget planner.
#The user enters monthly income, fixed expenses, variableexpenses,
#and savings percentage.
#Use arithmetic, comparison, and logicoperators to
#calculate total expenses, expected savings, remaining balance,
#and determine whether the user is staying within the recommended savings goal.

y=int(input("enter monthly income"))
x=int(input("enter fixed expenses"))
v=int(input("enter variable expenses"))
s=float(input("enter savings percentage"))
total_expense=x+v
e=s*y #expected savings
r=y-x-v-e #remianing balance
if r>=e:
    print("user is staying wihtin recommended savings goal")
else:
    print("user is not meeting his savings goal")
print("total_expense:", total_expense)
print("expected savings:",e)
print("remaining balance:",r)
