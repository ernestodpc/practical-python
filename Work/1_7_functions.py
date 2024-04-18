# 1.7 Functions
#
# As your programs start to get larger, you'll want to get organized.
# This section briefly introduces functions and library modules. Error handling
# with exceptions is also introduced.

# Custom functions
#
# Use functions for code you want to reuse. Here's a function definition:

def sumcount(n):
    '''
    Returns the sum of the first n integers
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
    
a = sumcount(100)

# A function is a series of statements that perform some task and return a result.
# The return keyword is needed to explicitly specify the return value of the
# function.


# Library functions
#
# Python comes with a large standard library. Library modules are accessed using
# import. For example:

import math

import urllib.request

u = urllib.request.urlopen('http://www.python.org/')

# Errors and exceptions
#
# Functions report errors as exceptions. An exception causes a function to abort
# and may cause your entire program to stop if unhandled.

# Try this in your Python REPL

int('N/A')

# Catching and Handling Exceptions
#
# Exceptions can be caught and handled.
# To catch, use the try-except statement

for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Could not parse", line)
    else:
        print("Code did no trigger any exception!")

try:
    x = (2 / 1)
except BaseException as e:
    print(e)
else:
    print("Code did not raise an exception!")

# Raising Exceptions
#
# To raise an exception use the raise statement
raise RuntimeError('What a kerfuffle!')

# This will cause the program to abort with an exception traceback. Unless
# caught by a try-except block

# Excercises
#
# 1.29: Defining a function
def greeting(name):
    'Issues a greeting'
    print('Hello', name)

greeting('Guido')

greeting('Paula')

# If the first statement of a function is a string, it serves as documentation.
# Try typing a command such as help(greeting) to see it displayed.

help(greeting)


