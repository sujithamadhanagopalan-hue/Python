mylist =[0,1,2,3,"a,b,c", [1,2,3]]
mylist.append("7")
print (mylist)
mylist.pop()
for i in mylist:
    print(i)

#append
mylist =[0,1,2,3,"a,b,c", [1,2,3]]
print (mylist)
mylist.pop()
for i in mylist:
    print(i)

#append - inlcude the number
#pop - remove last element

# 1. Get the list of items from the user
shopping_cart = input("Enter list of items (separated by commas): ").split(",")
shopping_cart = [item.strip() for item in shopping_cart]

# 2. Append 'cake' to the cart
shopping_cart.append("cake")
print("Current cart:", shopping_cart)

print("---")

# 3. Check for an essential item (e.g., rice)
essential_item = 'rice'
if essential_item in shopping_cart:
    print(f"Yes, {essential_item} is in your cart!")
else:
    print(f"{essential_item} is essential, please pick it up!")

print("---")

# 4. Search for a specific item
search = input("Enter the item you want to search for: ").strip()

# Initialize our tracker variable
found = False

# Loop through the cart to see if the searched item exists
for item in shopping_cart:
    if item.lower() == search.lower():  # .lower() makes it case-insensitive (e.g., 'Rice' matches 'rice')
        found = True
        break  # We found it, so we can stop searching!

# 5. Print the search results
if found:
    print(f"Success! '{search}' is in your list.")
else:
    print(f"Sorry, '{search}' was not found in your list.")
