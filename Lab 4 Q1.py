#Develop a Python program that records a user's
#daily expenses for an entire month. Using loops, calculate total spending,
#average daily expenditure, highest and lowest expenses, and identify days
#where spending exceeded a user-defined budget limit. Generate a monthly
#financial summary.

days = int(input("Enter number of days in the month: "))
budget = float(input("Enter your daily budget limit: "))

expenses = []

for day in range(1, days + 1):
    amount = float(input(f"Enter expense for Day {day}: "))
    expenses.append(amount)
total_spent = 0
highest_expense = expenses[0]
lowest_expense = expenses[0]
highest_day = 1
lowest_day = 1
over_budget_days = []

for index, amt in enumerate(expenses):
    day_num = index + 1
    total_spent += amt  # Add to total
    
    if amt > highest_expense:
        highest_expense = amt
        highest_day = day_num
        
    if amt < lowest_expense:
        lowest_expense = amt
        lowest_day = day_num
        
    if amt > budget:
        over_budget_days.append(day_num)

average_daily = total_spent / days

#summary report
print("MONTHLY SUMMARY")
print(f"Total Spending: Rs.{total_spent:.2f}")
print(f"Average Daily Expenditure: Rs.{average_daily:.2f}")
print(f"Highest Expense: Day {highest_day} (Rs.{highest_expense:.2f})")
print(f"Lowest Expense: Day {lowest_day} (Rs.{lowest_expense:.2f})")

print("\nBudget Analysis:")
if len(over_budget_days) > 0:
    print(f"Days you exceeded your budget: {over_budget_days}")
else:
    print("You stayed within budget every day!")
