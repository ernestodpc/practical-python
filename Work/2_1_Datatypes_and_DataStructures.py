# 2.1 Datatypes and Data structures
#
# This section introduces data structures in the form of tuples and dictionaries
#
# Primitive Datatypes
#
# Python has a few primitive types of data:
# * Integers
# * Floating point numbers
# * Strings (text)
#
# We learned about these in the introduction
#
# None type
email_address = None
# None is often used as a placeholder for optional or missing value. It evaluates as False in
# conditionals

if email_address:
    print(f'Sending email to: {email_address}')

# Data Structures
#
# Tuples
# A tuple is a collection of values grouped together
s = ('GOOG', 100, 490.1)

# Sometimes the () are omitted in the syntax
s = 'GOOG', 100, 490.1

# Special cases (0-tuple, 1-tuple)
t = ()   #An empty tuple
w = ('GOOG',) # A 1-item tuple

# Tuples are often used to represent simple records or structures.
# Typically, it is a single object of multiple parts. A good analogy:
# A tuple is like a single row in a database table.

# Tuple's contents are ordered (like an array)

name = s[0]
shares = s[1]
price = s[2]

# However, the contents cannot be modified
#s[1] = 75

# Tuple Packing
#
# Tuples are more about packing related items together into a single entity.
s = ('GOOG', 100, 490.1)

# Tuples vs Lists
#
# Tuples look like read-only lists. However, tuples are most often used
# for a single item consisting of multiple parts. Lists are actually a
# collection of disctinct items, usually all of the same type.

# Dictionaries
#
# A dictionary is mapping of keys to values. It's also sometimes called a
# hash table or associative array. The keys serve as indices for accessing values.

s = {
    'name':'GOOG',
    'shares':100,
    'price':490.1
    }

# Why dictionaries?
#
# Dictionaries are useful when there are many different values and those values
# might be modified or manipulated. Dictionaries make your code more readable

# Excercises

# 2.1 Tuples
# At the interactive prompt, create the following tuple that represents the
# above row, but with the numeric columns converted to proper numbers:
row = ['AA', '100', '32.20']

t = (row[0], int(row[1]), float(row[2]))
cost = t[1] * t[2]

# Is math broken in Python? What's the deal with the answer of 3220.000000000005?
#
# This is an artifact of the floating point hardware on your computer only being
# able to accurately represent decimals in Base-2, not Base-10. For even simple
# calculations involving base-10 decimals, small errors are introduced. This is
# normal, altough perhaps a bit surprising if you have not seen it before.

# Excercise 2.2: Dictionaries as a data structure
#
# An alternative to a tuple is to create a dictionary instead.
# Completed!

# Completed!

# Completed Section 2.1

