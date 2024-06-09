# 2.5 Collections Module

# The collections module provides a number of useful objects for data handling. This
# part briefly introduces some of these features

# Example: Counting things

# Let us say you want to tabulate the total shares of each stock:

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

# There are two IBM entries and two GOOG entries in this list.
# The shares need to be combined together somehow.

# Counters
#
# Solution: Use a Counter

from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares
    
total_shares['IBM']

# Example: One-Many Mappings
# Problem: You want to map a key to multiple values

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

# Like in the previous example, the key IBM should have two different
# tuples instead
#
# Solution: use a defaultdict

from collections import defaultdict


holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM']

# The defaultdict ensures that every time you access a key you get
# a default value.

# Example: Keeping a History
# Problem: We want a history of the last N things.
# Solution: Use a deque (double-ended-que)

#from collections import deque

#history = deque(maxlen=N)
#with open(filename) as f:
#    for line in f:
#        history.append(line)

# Exercises
#
# The collections module might be one of the most useful library
# modules for dealing with special purpose kinds of data-handling
# problems such as tabulating and indexing.

# In this exercise, we'll look at a few simple examples. Start
# by running your report.py program so that you have the portfolio
# of stocks loaded in interactive mode

# 2.18: Tabulating with Counters
#
# Suppose you wanted to tabulate the total number of shares of each
# stock. This is easy using Counter objects. Try it:

# Completed interactively!

# Carefully observe how the multiple entries for MSFT & IBM in portfolio
# get combined into a single entry here

# You can use a Counter just like a dictionary to retrieve individual values
# If you want to rank the values use the most common method of Counters

# Let's grab another portfolio of stocks and make a new Counter:
# Completed interactively

# Finally let's combine all of the holdings doing one simple operation
# concatenate both Counter objects: completed interactively

# This is only a small taste of what counters provide. However, if you ever
# find yourself needing to tabulate values, you should consider using one.

# Commentary: collections module
#
# The collections module is one of the most useful library modules in all
# of Python. In fact, we could do an extended tutorial on just that. However,
# doing so now would also be a distraction. For now, put collections on your
# list of bedtime reading for later.
