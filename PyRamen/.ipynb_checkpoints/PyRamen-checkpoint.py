# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path
# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')
# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []
# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as menu_file:
    csvreader = csv.reader(menu_file, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        menu.append(row)
# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as sales_file:
    csvreader = csv.reader(sales_file, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        sales.append(row)
# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}
# Initialize a row counter variable
row_count = 0
# @TODO: Loop over every row in the sales list object
for sale in sales:
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(sale[3])
    sales_item = sale[4]
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    report[sales_item] = {
                        "01-count": 0,
                        "02-revenue": 0,
                        "03-cogs": 0,
                        "04-profit": 0,
                        }
    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for menu_item in menu:
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        item = menu_item[0]
        price = float(menu_item[3])
        cost = float(menu_item[4])
        # @TODO: Calculate profit of each item in the menu data
        profit = price * quantity
        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if sales_item == item:
            # @TODO: Print out matching menu data
            print(sales_item)
            print(item)
            # @TODO: Cumulatively add up the metrics for each item key
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print(f"{sales_item} does not equal {item}! NO MATCH!")
    # @TODO: Increment the row counter by 1
    row_count  += 1

# @TODO: Print total number of records in sales data
print(row_count)
# @TODO: Write out report to a text file (won't appear on the command line output)
output_path = Path("output.txt")
with open(output_path, 'w') as file:
    for line in report:
        print(line)
        file.write(line + "\n")