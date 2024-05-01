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
        portfolio = [{'name':name, 'shares':int(shares), 'price':float(price)} for name, shares, price in reader]
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

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

portfolio_cost = 0.0
for stock in portfolio:
    portfolio_cost += stock.get('shares') * stock.get('price')
print(f'portfolio_cost: {portfolio_cost}')

portfolio_value = 0.0
for stock in portfolio:
    portfolio_value += stock.get('shares') * prices[stock.get('name')]
print(f'portfolio_value: {portfolio_value}')

print(f'The gain (or loss) is: {portfolio_value - portfolio_cost}')
