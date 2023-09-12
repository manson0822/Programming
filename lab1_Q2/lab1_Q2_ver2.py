################################################################################
# The name and the price of each dish is determined by input
# Suppose that the number of dishes in each column is identical
################################################################################

# Obtain the store name and its field width
store_name = input()
fieldwidth = int(input())

# Print the store name
print (f"{store_name:^{fieldwidth}}")
print ()

# Obtain the number of columns, the name of each category, and the width of each column
column_cnt = int(input())
column_names = input().split()
column_fieldwidths = [int(x) for x in input().split()]

# Print categories
for i in range(column_cnt):
    print(f"{column_names[i]:^{column_fieldwidths[i]}}", end = '')
print()

# Obtain the name and the price of each dish
rows_cnt_each_column = [int(x) for x in input().split()]
text_width_before_dollar = int(input())
rows_cnt_prefix_sum = [sum(rows_cnt_each_column[0:i]) for i in range(column_cnt)]
dish_names = input().split()
dish_prices = [float(x) for x in input().split()]

# Print the dishes
for i in range(max(rows_cnt_each_column) * column_cnt):
    row = i // column_cnt
    column = i % column_cnt
    if row < rows_cnt_each_column[column]:
        cnt = rows_cnt_prefix_sum[column] + row
        dash_cnt = text_width_before_dollar - len(str(cnt+1)) - 1 - len(dish_names[cnt])- len(f'{dish_prices[cnt]:.2f}') + 4
        text = f'{cnt+1}.{dish_names[cnt]}{"-" * dash_cnt}${dish_prices[cnt]:.2f}'
    else:
        text = ''
    print(f"{text:^{column_fieldwidths[column]}}", end = '')
    if column == column_cnt - 1:
        print()