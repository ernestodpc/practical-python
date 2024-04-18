# pcost.py
#
# Excercise 1.27: Reading a data file
#
#Now that you know how to read a file, let us write a program to perform
#a simple calculation.
#
#The columns in portfolio.csv correspond to the stock name, number of shares,
#and purchase price of a single stock holding. Write a program called pcost.py
#that opens this file, reads all lines, and calculates how much it cost to purchase
#all of the shares in the portfolio.

# Hint: to convert a string to an integer, use int(s). To convert a string to a
# floating point, use float(s).

# Your program should print output such as the following:
# Total cost 44671.15

#with open('Work/Data/portfolio.csv', 'rt') as f:
#    next(f)
#    sum = 0
#    for line in f:
#        row = line.split(',')
#        _, n_shares, share_price = row
#        sum = sum + int(n_shares) * float(share_price)
#    print(f'Total cost {sum:.2f}')
#
# Excercise 1.30: Turning a script into a function
#
# Take the code you wrote for the pcost.py program in excercise 1.27 and turn it into
# a function portfolio_cost(filename). This function takes a filename as input, reads
# the portfolio data in that file, and returns the total cost of the portfolio as a
# float.

# To use your function, change your program so that it looks something like this:

#def portfolio_cost(filename: str) -> float:
#    '''Read input filename and return the total cost of the portfolio as a float.
#       If the input file is not found return None'''
#    try:
#        with open(filename, 'rt') as f:
#            next(f)
#            sum = 0
#            for line in f:
#                row = line.split(',')
#                _, n_shares, share_price = row
#                try:
#                    sum = sum + int(n_shares) * float(share_price)
#                except ValueError as e:
#                    print('Warning ValueError', e)
#                    continue
#            return sum
#    except FileNotFoundError as e:
#        print(e)
#        return None
#
#
#
#cost = portfolio_cost('Work/Data/portfolio.csv')
#print('Total cost:', cost)
#


# When you run your program, you should see the same output as before. After you've run
# your program, you can also call your function interactively by typing this:
# bash $ python3 -i pcost.py
# This will allow you to call your function from the interactive mode.
# Being able to experiment with your code interactively is useful for testing and debugging.

# Excercise 1.31: Error handling
#
# What happens if you try your function on a file with some missing fields?
# Modify the pcost.py program to catch the exception, print a warning message, and
# continue processing the rest of the file.
# COMPLETE!

# Excercise 1.32: Using a library function
#
# Python comes with a large standard library of useful functions. One library
# that might be useful here is the csv module. You should use it whenever you have
# to work with CSV data files. Here's an example of how it works...

# Modify your pcost.py program so that it uses the csv module for parsing and try
# running earlier examples. ---> Complete!

# Excercise 1.33: Using Reading from the command line ---> Done! program should be run
# from the terminal!

import csv

import sys

def portfolio_cost(filename: str) -> float:
    '''Read input file name and return the total cost of the portfolio as float.'''
    with open(filename, newline='') as file:
        csv_reader = csv.reader(file)
        next(file)
        sum = 0
        for row in csv_reader:
            _name, shares, price = row
            try:
                sum += int(shares) * float(price)
            except ValueError as e:
                print('Warning ValueError', e)
                continue
        return sum


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Daata/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

