menu_items = [
    [1, "Chicken Strips", 3.75], [2, "French Fries", 2.50],
    [3, "Hamburger", 4.00], [4, "Hot Dog", 3.50], [5, "Large Drink", 1.75],
    [6, "Medium Drink", 1.50], [7, "Milk Shake", 2.25], [8, "Salad", 4.25],
    [9, "Small Drink", 1.25]
]

print("Menu")
for item in menu_items:
    print('{} {} - {:.2f}'.format(*item))

order = raw_input('\n\nPlease enter the numbers of the items you would like: ')

print("You ordered: ", order)

order_total = 0

for item in order:
    print(menu_items[int(item) - 1])
