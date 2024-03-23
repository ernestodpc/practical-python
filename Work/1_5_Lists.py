
# 1.5 Lists
#
# This section introduces lists, Python's primary type for holding an ordered collection of values.

# Creating a List

names = [ 'Elwood', 'Jake', 'Curtis']

nums = [ 39, 38, 42, 65, 111]

# Sometimes lists are created by other methods. For example,

try:
    names.index('Ernesto')
except ValueError as e:
    print(e)
else:
    print('try block executed without exceptions!')

# Excercises

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

symlist


 = symbols.split(',')

# Excercise 1.19: Extracting and reassigning list elements

symlist


[0]

symlist


[1]

symlist


[-1]

symlist


[-2]

# Try reassigning one value:

symlist


[2] = 'AIG'

symlist




# Take a few slices:

symlist


[0:3]

symlist


[-2:]

# Create an empty list and append an item to it:

mysyms = []

mysyms.append('GOOG')

mysyms

# You can reassig a portion of a list to another list:

symlist


[-2:] = mysyms

symlist





# Excercise 1.20: Looping over list items

for s in symlist


:
    print('s =', s)

# Excercise 1.21: Membership tests

# Use the in or not in operator to check if 'AIG', 'AA', and 'CAT' are in the list of symbols

'AIG' in symlist



'AA' in symlist

'CAT' not in symlist

# Excercise 1.22: Appending, inserting and deleting items

symlist.append('RHT')


symlist.remove('MSFT')

symlist.append('YHOO')

symlist.index('YHOO')

symlist[1:2] = ['AA']

symlist.index('YHOO')

symlist[1:3] = ['AA', 'AAPL']

symlist.index('YHOO')

symlist

symlist[3:5] = ['AIG', 'YHOO']

symlist.index('YHOO')

symlist.insert(4, 'YHOO')

del symlist[4]

symlist.count('YHOO')

symlist.sort()

symlist

symlist.insert(3, 'GOOG')

symlist.remove('YHOO')

symlist

symlist.sort(reverse = True)

symlist

#Excercise 1.24: Putting it all back together
#
#Want to take a list of strings and join them together into one string?
#Use the join() method of strings like this(note: this looks funny at first)

a = ','.join(symlist)

a

b = ':'.join(symlist)

b

c = ''.join(symlist)

'juan_'.join(symlist)


#Excersise 1.25: Lists of anything
#
#Lists can contain any kind of object, including other lists:

nums = [101, 102, 103]


items = ['spam', symlist, nums]

items

#Even though it is technically possible to make very complicated list structures
#as a general rule, you want to keep things simple. Usually lists hold items that
#are all the same kind of value. For example, a list that consists entirely of
#numbers or a list of text strings. Mixing different kinds of data together in the
#same list is often a good way to make your head explode so it's best avoided.


