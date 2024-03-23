# Excercise 1.15: Membership testing (substring testing)

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'

'IBM' in symbols

'AA' in symbols

'CAT' in symbols

#Why did the check for 'AA' return True?

#Because AA is a substring of symbols.

# Excercise 1.16: String Methods
symbols.lower()

symbols

#Remember, strings are always read-only. If you want to save the result
#of an operation, you need to place it in a variable

lowersyms = symbols.lower()

lowersyms

#Try some more operations:

symbols.find('MSFT')

symbols[13:17]

symbols = symbols.replace('SCO', 'DOA')

symbols

name = '    IBM    \n'

name = name.strip()

name

"\n" in name

#Excercise 1.17: f-strings
#
#Sometimes you want to create a string and embed the values of variables into it.
#To do that, use and f-string. For example:

name = 'IBM'

shares = 100

price = 91.1

f'{shares} shares of {name} at ${price:0.2f}'



#Completed excercise: Modify the mortgage.py program from Ex 1.10 to create
#its output using f-strings. Try to make it so that output is nicely aligned.


#Excercise 1.18: Regular Expressions
#
#One limitation of the basic string operations is that they don't support
#any kind of advanced pattern matching. For that, you need to turn to
#Python's re module and regular expressions. Regular expression handling is
#a big topic, but here's a short example

text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'

import re

re.findall(r'\d+/\d+/\d+', text)

#Replace all occurences of a date with replacement text

re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
