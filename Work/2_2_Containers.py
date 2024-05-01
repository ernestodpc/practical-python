# 2.2 Containers
#
# This section discusses lists, dictionaries, and sets.

# Overview
#
# Programs often have to work with many objects
#     A portfolio of stocks
#     A table of stock prices
#
# There are three main choices to use:
#     Lists: Ordered data
#     Dictionaries: Unordered data
#     Sets: Unordered collection of unique items

# Lists as a Container
#     * Use a list when the order of the data matters. Remember that lists can hold any kind of object.
#       For example, a list of tuples.

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
    ]

portfolio[0]
portfolio[1]
portfolio[2]

# List construction
#
# Building a list from scratch
records = [] #Initial empty list

# Use .append() to add more items
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
records.append(('CAT', 150, 83.44))


# Dicts as a Container
#
# Dictionaries are useful if you want fast random lookups (by keyname). For example,
# a dictionary of stock prices:

prices = {
    'GOOG':513.25,
    'CAT':87.22,
    'IBM': 93.37,
    'MSFT': 44.12
    }

# Here are some simple lookups:
prices.get('IBM', 999)

# Composite keys
#
# Almost any type of value can be used as a dictionary key in Python. A dictionary
# key must be of a type that is immutable. For example, tuples:

holidays = {
    (1, 1):'New Years',
    (3, 14):'Pi day',
    (9, 13):"Programmer's day",
    }


# Sets
#
# Sets are a collection of unordered unique items

tech_stock = { 'IBM', 'AAPL', 'MSFT' }
#
# alternative syntax
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])

# Excercises
# In these exercises, you start building one of the major programs used for
# the rest of this course. Do your work in the file Work/report.py


