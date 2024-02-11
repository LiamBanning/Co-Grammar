# Creates a list of items, and an empty list to append values to
menu = ["Cake", "Sausage Roll", "Chips", "Sandwich"]
total_value = []

# Creates 2 dictionaries for stock and price, indexing the menu list to create keys and ensure reusability
stock = {menu[0]: 2.00, menu[1]: 5.00, menu[2]: 3.00, menu[3]: 8.00}

price = {menu[0]: 2.50, menu[1]: 1.45, menu[2]: 2.00, menu[3]: 3.45}

# For loop that iterates through menu items, multiplies stock and price values
# and appends to the total_value list
for i in menu:
    item_value = (stock[i] * price[i])
    total_value.append(item_value)

# Prints the total value from the total_value list
print(sum(total_value))
