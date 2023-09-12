# You can either use these variables or create your own dishes
names = [['hamburger', 'Omelette', 'toast', 'waffle'], ['hamburger', 'Omelette', 'toast', 'waffle'], ['hamburger', 'Omelette', 'toast', 'waffle']]
prices = [[7.993, 5.49, 2.09, 6.49], [7.993, 5.49, 2.09, 6.49], [7.993, 5.49, 2.09, 6.49]]

# hamburger = 7.993
# Omelette = 5.49
# toast = 2.09
# waffle = 6.49
# wraps = 9.59
# paninis = 8.29
# sandwich = 7.49
# black_tea = 1.49
# juice = 1.99
# milk_tea = 2.99
# soft_drink = 2.99

# Print the store name ( you need to change the store name )
print ( f" { ' manson Cafe Brunch ':^90} " )
print ()
# Print the categories ( you may change categories )
# for loops
print ( f" { ' Breakfast ':^30}{ ' Lunch ':^27}{ ' Beverages ':^35} " )

# Try to print the rest of the menu ...
print("1.Burgers----------$7.99 2.Wraps------------$9.59 3.Green Tea--------$1.49")

for i in range(4):
    # print(f" { f'{names[0][i]}: ${prices[0][i]}':<30}{ f'{names[1][i]}: ${prices[0][i]}':<27}{ f'{names[2][i]}: ${prices[0][i]}':<35} ")



# print ( f" { ' hamburger ':<30}{ ' wraps ':<27}{ ' black_tea ':<35} " )
# print ( f" { ' Omelette ':<30}{ ' paninis ':<27}{ f' juice: {juice} ':<35} " )
# print ( f" { ' toast ':<30}{ ' sandwich ':<27}{ ' milk_tea ':<35} " )
# You can see the result below as a reference