
inventory = {
    "Laptop": 10,
    "Headphones": 25,
    "Smartphone": 15,
    "Smartwatch": 20
}

prices = {
    "Laptop": 1000.00,
    "Headphones": 150.00,
    "Smartphone": 700.00,
    "Smartwatch": 250.00
}


total_units_sold = {
    "Laptop": 0,
    "Headphones": 0,
    "Smartphone": 0,
    "Smartwatch": 0
}

cumulative_revenue = 0.0
day_counter = 1
running = True

print("Online store administration")


while running:
    print(f"STARTING BUSINESS: DAY {day_counter}")
    
    daily_revenue = 0.0
    processing_orders = True
    
    while processing_orders:
        print("\n Current Inventory Levels")
        for item, stock in inventory.items():
            print(f"  {item}: {stock} available")
    
        print("Menu: [1] Process New Order | [2] Close Day | [3] Terminate Program")
        choice = input("Select an option: ")
        
        if choice == "1":
            product = input("Enter product name to buy: ").strip()
            
            if product in inventory:
                quantity = int(input(f"Enter quantity of {product}s: "))
                
                if inventory[product] >= quantity:
                
                    inventory[product] -= quantity
                    
                    order_cost = quantity * prices[product]
                    daily_revenue += order_cost
                    cumulative_revenue += order_cost
                    
                    total_units_sold[product] += quantity
                    
                    print(f"Success! Order processed. Total: ${order_cost:.2f}")
                else:
                    print(f"Order Failed: Not enough stock! Only {inventory[product]} left.")
            else:
                print("Invalid product name. Please check spelling.")
                
        elif choice == "2":
            print(f"\n Closing out Day {day_counter}...")
            processing_orders = False  
            
        elif choice == "3":
            print("\nInitiating emergency system shutdown...")
            processing_orders = False
            running = False            
            
        else:
            print("Invalid selection. Choose 1, 2, or 3.")

    # -
    print(f"Daily report: DAY {day_counter}")
    print(f"Daily Revenue: Rs.{daily_revenue:.2f}")
    print(f"Cumulative Revenue so far: Rs.{cumulative_revenue:.2f}")
    
    day_counter += 1

print("\n" + "="*45)
print(" final performance")
print("="*45)
print(f"Total Days Operated  : {day_counter - 1}")
print(f"Total Global Revenue : ${cumulative_revenue:.2f}")

best_seller = "None"
max_sold = -1
for product, units in total_units_sold.items():
    if units > max_sold:
        max_sold = units
        best_seller = product

print(f"Best Selling Product : {best_seller} ({max_sold} units sold)")

print("\nLow Stock Alerts (Items with less than 3 remaining):")
low_stock_found = False
for product, stock in inventory.items():
    if stock < 3:
        print(f"ALERT: {product} is critically low! Only {stock} left.")
        low_stock_found = True

if not low_stock_found:
    print(" All inventory levels are healthy.")
print("="*45)
