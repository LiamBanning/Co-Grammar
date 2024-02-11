menu = ["Cake", "Sausage Roll", "Chips", "Sandwich"]
total_value = []

stock = {menu[0]: 2.00, menu[1]: 5.00, menu[2]: 3.00, menu[3]: 8.00}

price = {menu[0]: 2.50, menu[1]: 1.45, menu[2]: 2.00, menu[3]: 3.45}

for i in menu:
    item_value = (stock[i] * price[i])
    total_value.append(item_value)

print(sum(total_value))
