# 2.4 Sequences
#
# Sequence Datatypes
# Python has three sequence datatypes
#
#    * String: An immutable sequence of characters
#    * List: A mutable sequence of objects?
#    * Tuple: An immutable sequence of objects
#
# All sequences are ordered, indexed by integers, and have a length

a = 'Hello'
b = [1, 4, 5]
c = ('GOOG', 100, 490.1)

a[0]
b[-1]
c[1]

len(a)
len(b)
len(c)

# Sequences can be replicated s * n
a = 'Hello'
a * 3

b * 2

# Sequences of the same type can be concatenated
a = 1, 2, 3
b = (4, 5)


# Slicing
#
# Slicing means to take a subsequence from a sequence. The syntax is s[start:end].
# Where start and end are indexes of the subsequence you want
a = [i for i in range(9)]
a[2:5]
a[-5:]
a[:3]
#
# Indices start and end must be integers
# Slices do not include the end value. It's like a half-open interval from math.
# If indices are omitted, they default to the beginning or end of a list

# Slice re-assignment
#
# On lists, slices can be reassigned and deleted

a = [ i for i in range(9)]
print(a)
a[2:4] = [10, 11, 12]
print(a)

# Note: the reassigned slice does not need to have the same lenght

# Deletion
a = [i for i in range(9)]

del a[2:4]

print(a)

# Sequence Reductions
#
# There are some common functions to reduce a sequence to a single value

s = [i for i in range(1,5,1)]
sum(s)
min(s)
max(s)
t = ['Hello', 'World']
max(t)


# Iteration over a sequence
#
# The for loop iterates over the elements of a sequence

for i in s:
    print(i)

# On each iteration of the loop, you get a new item to work with. This new
# value is placed into the iteration variable. In this example the iteration
# variable is x:

for x in s:
    pass

# On each iteration, the previous value of the iteration variable is overwritten (if any).
# After the loop finishes, the variable retains the last value.

print(i)

# break statement
#
# You can use the break statement to break out of a loop early.
for i in range(5):
    print(i)
    break
else:
    print(f'The loop has been executed completely!')

# When the break statement executes, it exists the loop and moves on the next statements.
# The break statement only applies to the inner-most loop. If this loop is within another
# loop, it will not break the outer loop.

# continue statement
#
# To skip one element and move to the next one, use the continue statement.
# This is useful when the current item is not of interest or needs to be ignored in
# the processing.

# Looping over integers
#
# If you need to count, use range()
# The syntax is: range([start,] end [,step])
# The ending value is never included. It mirrors the behaviour of slices
# start is optional. Default 0
# step is optional. Default 1
# range() computes values as required. It does not actually store a large range of values.

# enumerate() function
#
# The enumerate function adds an extra counter value to iteration.
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    print(i, name)

# The general form is enumerate(sequence [, start = 0]). start is optional.
# A good example of using enumerate() is tracking line numbers while reading a file:
# In the end enumerate is just a nice shortcut for ...
# Using enumerate is less typing and runs slightly faster.

# For and tuples
#
# You can iterate with multiple iteration values
# When using multiple variables, each tuple is UNPACKED into a set of
# iteration values. The number of variables must match the number of items
# in each tuple.

# zip() function
#
# The zip function takes multiple sequences and makes an iterator that combines them
columns = ['name', 'shares', 'price']
values = ('GOOG', 100, 490.1)
pairs = zip(columns, values)

# To get the result you must iterate. You can use multiple variables to unpack the
# tuples as shown earlier.

# A common use of zip is to create key/value pairs for constructing dictionaries
d = dict(zip(columns, values))

# Excercises
#
# Excercise 2.13: Counting
# Try some basic counting examples:
for i in range(10):
    print(i, end='')

for n in range(10, 0, -1):
    print(n, end=' ')

for n in range(0, 10, 2):
    print(n, end=' ')

# Excercise 2.14: More sequence operations
#
# Interactively experiment with some of the sequence-reduction operations.
#
data = [4, 9, 1, 25, 16, 100, 49]
min(data)
max(data)
sum(data)
# Try looping over the data:
for x in data:
    print(x)

for n, x in enumerate(data):
    print(n, x)

# Sometimes the for statement, len(), and range() get used by novices in some kind
# of horrible code fragment that looks like it emerged from the depths of a rusty
# C program:

for n in range(len(data)):
    print(data[n])

# DO NOT DO THAT! Not only does reading it make everyone's eye bleed, it's inefficient
# with memory and it runs a lot slower. Just use a normal for loop if you want to
# iterate over the data. Use enumerate if you happen to need the index for some reason!

# Excercise 2.15: A practical enumerate() example
#
# Recall that the file Data/missing.csv contains data for a stock portfolio, but has
# some rows with missing data. Using enumerate(), modify your pcost.py program so that
# it prints a line number with the warning message when it encounters bad input.
# Excercise completed: see pcost.py

# Excercise 2.16: Using the zip() function completed: see report.py

# Excercise 2.17: Inverting a dictionary
#
# A dictionary maps keys to values. For example, a dictionary of stock prices
prices = {
    'GOOG': 490.1,
    'AA': 23.45,
    'IBM': 91.1,
    'MSFT': 34.23
    }

# if you use the items() method, you can get (key,value) pairs
prices.items()

# however, what if you wanted to get a list of (value, key) pairs instead?
# Use zip()
pricelist = list(zip(prices.values(), prices.keys()))

# Why would you do this? For one, it allows you to perform certain kinds
# of data processing on the dictionary data

min(pricelist)

max(pricelist)

sorted(pricelist)

# This also ilustrates an important feature of tuples. When used in comparisons,
# tuples are compared element-by-element starting with the first item. Similar
# to how strings are compared character-by-character.

# zip() is often used in situations like this where you need to pair up data
# from different places. For example, pairing up the column names with column
# values in order to make a dictionary of named values.

# Note: zip() is not limited to pairs. For example, you can use it with any
# number of input lists

a = [i for i in range(1,5,1)]

b = ['w', 'x', 'y', 'z']

c = [0.20, 0.40, 0.60, 0.80]

list(zip(a,b,c))

# Also, be aware that zip() stops once the shortest input sequence is exhausted
a = [i for i in range(1,7,1)]
b = ['x', 'y', 'z']

list(zip(a,b))


