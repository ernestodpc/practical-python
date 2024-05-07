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

# Excercise 2.15: A practical enumerate() example
#
# Recall that the file Data/missing.csv contains data for a stock portfolio, but has
# some rows with missing data. Using enumerate(), modify your pcost.py program so that
# it prints a line number with the warning message when it encounters bad input.
# Excercise completed!

#def portfolio_cost(filename: str) -> float:
#    '''Read input file name and return the total cost of the portfolio as float.'''
#    with open(filename, newline='') as file:
#        csv_reader = csv.reader(file)
#        next(file)
#        sum = 0
#        for rowno, row  in enumerate(csv_reader, start=1):
#            _name, shares, price = row
#            try:
#                sum += int(shares) * float(price)
#            except ValueError:
#                print(f'Row {rowno}: Bad row: {row}')
#                continue
#        return sum
#
#
#if len(sys.argv) == 2:
#    filename = sys.argv[1]
#else:
#    filename = 'Work/Data/portfolio.csv'
#
#cost = portfolio_cost(filename)
#print('Total cost:', cost)
#
# Excercise 2.16: Using the zip() function
#
# In the file Data/portfolio.csv, the first line contains column headers. In all
# previous code, we've been discarding them. However, what if you could use the
# headers for something useful? This is where the zip() function enters the picture.
# First try to pair the file headers with a row of data...
# ...
# Notice how zip() paired the column headers with the column headers. We've used lis()
# here to turn the result into a list so that you can see it. Normally, zip() creates
# an iterator that must be consumed with a for loop.

# This pairing is an intermediate step to building a dictionary. Now try this
# record = dict(zip(headers, row))
# This transformation is one of the most useful tricks to know about when processing a lot
# of data files. For example, suppose you wanted to make the pcost.py program to work with
# various input files, but without regard for the actual column number where the name, shares,
# and price appear.
#
# Modify the portfolio_cost() function in pcost.py so that it looks like this ...
def portfolio_cost(filename: str) -> float:
    '''Read input file name and return the total cost of the portfolio as float.'''
    with open(filename, newline='') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        sum = 0
        for rowno, row  in enumerate(csv_reader, start=1):
            record = dict(zip(headers, row))
            try:
                sum += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
                continue
        return sum


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

# If you did it right, you'll find that your program still workd even though the data has a completely
# different column format than before. That's cool!
# The change made here is subtle, but significant. Instead of portfolio_cost() being hard-coded to
# read a single fixed file format, the new version reads any CSV file and picks the values of interest
# out of it. As long as the file has the required columns, the code will work.
# Modify the report.py program that you wrote in Section 2.3 so that it uses the same technique
# to pick out column headers.
# Try running the report.py program on the Data/portfoliodate.csv file and see that it produces the
# same answer as before.
