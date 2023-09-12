# You can either use these variables or create your own dishes
names = [['hamburger', 'Omelette', 'toast', 'waffle'], ['wraps', 'paninis', 'sandwich', 'noodles'], ['black_tea', 'juice', 'milk_tea', 'soft_drink']]
prices = [[7.993, 5.49, 2.09, 6.49], [9.59, 8.29, 7.49, 7.89], [1.49, 1.99, 2.99, 2.99]]
fieldwidths = [30, 27, 35]

# Print the store name ( you need to change the store name )
print ( f"{'manson Cafe Brunch':^90}" )
print ()
# Print the categories ( you may change categories )
# for loops
print ( f"{'Breakfast':^30}{'Lunch':^27}{'Beverages':^35} " )

# Try to print the rest of the menu ...
# print("1.Burgers----------$7.99 2.Wraps------------$9.59 3.Green Tea--------$1.49")

for i in range(4):
    for j in range(3):
        text = f'{i * 3 + j + 1}.{names[j][i]}{"-" * (20-len(str(i * 3 + j + 1))-1-len(names[j][i]))}${prices[j][i]:.2f}'
        print(f"{text:^{fieldwidths[j]}}", end = '')
    print()