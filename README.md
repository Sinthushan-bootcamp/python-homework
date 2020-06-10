# python-homework

## Pybank
* This script takes in a csv with profit and loss information for an imaginary company. 
* The csv file consist of two columns, date, and profit/loass
* the script then returns the following:
    * Total Months
    * Total
    * Average Change
    * Greatest Increase in Profits
    * Greatest Decrease in Profits
### Dependencies 
* [pathlib](https://docs.python.org/3/library/pathlib.html)
* [csv](https://docs.python.org/3/library/csv.html)

## PyRamen
* This script takes in two CSVs one with sales data and one with menu data for a fake resteraunt
* The script then calculates the quantity, revenue, cost, and profit on a per menue item basis
* The script does so by:
    * Initialize report dicionary
    * Loop through all sales items
    * if sales item is not in dictionary initialize a new dictionary item within report dictionary for sales item
    * for every iteration of sales item loop through the rows in the menu csv and calculate revenue, cost, and profit and accumulate the values for the relevent keys in the dictionary   
### Dependencies 
* [pathlib](https://docs.python.org/3/library/pathlib.html)
* [csv](https://docs.python.org/3/library/csv.html)