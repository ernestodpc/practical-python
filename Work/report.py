# report.py
#
# Exercise 2.4: A list of tuples
# The file Data/portfolio.csv contains a list of stocks in a portfolio.
# In exercise 1.30, you wrote a function portfolio_cost(filename) that
# read this file and performed a simple calculation.

# Your code should have looked something like this

#import csv
#
#
#def portfolio_cost(filename):
#    '''Computes the total cost (shares*price) of a portfolio file'''
#    total_cost = 0.0
#
#    with open(filename, 'rt) as f:
#        rows = csv.reader(f)
#        headers = next(rows)
#        for row in rows:
#            nshares = int(row[1])
#            price = float(row[2])
#            total_cost += nshares * price
#    return total_cost
#
# Using this code as a rough guide, create a new report.py
# In that file, define a function read_portfolio(filename)
# that opens a given portfolio file and reads it into a list of tuples.
# To do this, you're going to make a few minor modifications to the above
# code.
#
# First, instead of defining total_cost = 0,  you'll make a variable that's
# initially set to an empty list. For example:
# portfolio = []
#
# Next, instead of totaling up the cost, you'll turn each row into a tuple
# exactly

import csv

from pathlib import Path

def read_portfolio(filename):
    '''Reads filename and returns a list of tuples with'''
    file_path = Path(filename)
    portfolio = []
    with file_path.open() as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            share, shares, price  = row
            portfolio.append(tuple([share, int(shares), float(price)]))
        return portfolio


# Excercise 2.5: List of Dictionaries
#
# Take the function you wrote in Ex 2.24 and modify to represent each stock in
# the portfolio with a dictionary instead of a tuple. In this dict use the field
# names of "name", "shares", and "price" to represent the different columns in the
# input file

def read_portfolio(filename):
    '''Reads filename and returns a list of dictionaries with
    the following keys: "name", "shares", and "price"'''
    file_path = Path(filename)
    with file_path.open() as f:
        reader = csv.reader(f)
        headers = next(reader)
        #portfolio = [{'name':name, 'shares':int(shares), 'price':float(price)} for name, shares, price in reader]
        portfolio = [dict(zip(headers, row)) for row in reader]
    return portfolio

# Excercise 2.6: Dictionaries as containers
#
# A dictionary is a useful way to keep track of items where you want to look up items using an index
# other than an integer. In the Python shell try...

# Write a function read_prices(filename) that reads a set of prices such as this into a dictionary
# where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
# The other little complication is that the 'Data/prices.csv' file may have some blank lines in it. Notice
# how the last row of data above is an empty list - meaning no data was present on that line.
#
# There's a possibility that this could cause your program to die with an exception. Use the try and except
# statements to catch this as appropriate. Thought: would it be better to guard against bad data with
# an if statements instead???

# Once you've written your read_prices() function, test it interactively to make sure it works

def read_prices(filename):
    '''Reads a set of name, price data into a dictionary'''
    file_path = Path(filename)
    with file_path.open() as f:
        reader = csv.reader(f)
        my_dict = dict((row[0], float(row[1])) if row else (None,0) for row in reader)
        return my_dict

# Excercise 2.7: Finding out if you can retire
#
# Tie all of this work together by adding a few additional statements to your report.py
# program that computes the gain/loss (ratio). These statements should take the list of
# stocks in Ex 2.5 and the dictionary of prices in Ex 2.6 and compute the current value
# of the portfolio along with the gain/loss

portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

portfolio_cost = 0.0
for stock in portfolio:
    portfolio_cost += int(stock.get('shares')) * float(stock.get('price'))
print(f'portfolio_cost: {portfolio_cost}')

portfolio_value = 0.0
for stock in portfolio:
    portfolio_value += int(stock.get('shares')) * float(prices[stock.get('name')])
print(f'portfolio_value: {portfolio_value}')

print(f'The gain (or loss) is: {portfolio_value - portfolio_cost}')


# Excercise 2.9: Collecting Data
#
# In Excercise 2.7, you wrote a program called report.py
# that computed the gain/loss of a stock portfolio. In this
# excercise, you're going to start modifying it to produce a table
# like this:
# ...
# In order to generate the above report, you'll first want to collect
# all of the data shown in the table. Write a function make_report()
# that takes a list of stocks and a dictionary of prices as inputs and
# returns a list of tuples containing the rows of the above table.

def make_report(*, stock_list, prices_dict):
    '''What am I supposed to do???'''
    my_report = [(stock.get('name'), int(stock.get('shares')),
                  prices_dict.get(stock.get('name')),
                  prices_dict.get(stock.get('name')) - float(stock.get('price')))
                 for stock in stock_list]
    return my_report

my_report = make_report(stock_list=portfolio, prices_dict=prices)

# Excercise 2.10: Printing a formatted table
#
# Have your program take the output of the make_report() function
# and print a nicely formatted table as shown

def print_report(*, report):
    '''I have no idea what I'm doing!'''
    print('\n')
    for name, shares, price, change in report:
        my_string = f'{name:>10s} {shares:>10d} {price:>10.2f} {change:10.2f}'
        print(my_string)

print_report(report=my_report)

# Excercise 2.11: Adding some headers
#
# Add code to your program that takes a tuple of headers and creates
# a string where each header name is right-aligned in a 10-character
# wide field and each field is separated by a single space.

def print_report(*, report, headers, sep=None):
    '''I have no idea what I'm doing!'''
    print('\n')
    name, shares, price, change, *_ = headers
    header_string = f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}'
    print(header_string)
    sep_string = f'{10*sep:>10s} {10*sep:>10s} {10*sep:>10s} {10*sep:>10s}'
    print(sep_string)
    currency_symbol = '$'
    for name, shares, price, change in report:
        price = currency_symbol+f'{price:.2f}'
        my_string = f'{name:>10s} {shares:>10d} {price:>10s} {change:10.2f}'
        print(my_string)

print_report(report=my_report, headers=('Name', 'Shares', 'Price', 'Change'), sep='-')

# Excercise 2.12: Formatting challenge
#
# How would you modify your code so that the price includes the currency symbol ($)?
# Completed! see above function definition!

# Excercise 2.16 using the zip function ---> Completed
# Modify the report.py program that you wrote in Section 2.3 so that it uses the same technique
# to pick out column headers.
# Try running the report.py program on the Data/portfoliodate.csv file and see that it produces the
# same answer as before.
