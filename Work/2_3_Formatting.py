# 2.3 Formatting
#
# This section is a slight digression, but when you work with
# data, you often want to produce structured output(tables, etc.).

# String Formatting
#
# One way to format string in Python 3.6+ is with f-strings.
name = 'IBM'
shares = 100
price = 91.1

f'{name:>10s} {shares:>10d} {price:>10.2f}'

# The part {expression:format} is replaced.
# It is commonly used with print

print(f'{name:>10s} {shares:>10d} {price:>10.2f}')

# Format codes
#
# Format codes (after the : inside the {}) are similar to C printf().
# Common codes include:
#
# d Decimal Integer
# b Binary Integer
# x Hexadecimal Integer
# f Float as [-]m.ddddd
# e Float as [-]m.ddddde+-xx
# g Float, but selective use of E notation
# s String
# c Character (from integer)

# Common modifiers adjust the field width and decimal precision. This is
# a partial list:
#
# :>10d Integer right-aligned in a 10-character field
# :<10d Integer left-aligned in a 10-character field
# :^10d Integer centered in a 10-character field
# :0.2f Float with 2-digit precision

# Dictionary Formatting
#
# You can use the format_map() method to apply string formatting to a dictionary
# of values

s = {
    'name':'IBM',
    'shares':100,
    'price':91.1
    }

'{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)

# It uses the same codes as f-strings but takes the values from
# the supplied dictionary

# format() method
#
# There is a method format() that can apply formatting to arguments
# or keyword arguments
'{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1)

print('{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1))

# Frankly, format() is a bit verbose. I prefer f-strings

# C-Style formatting
#
# You can also use the formatting operator %

print('The value is %d' % 3)

'%5d %-5d %10d' % (3, 4, 5)

'%0.2f' % (3.1415926,)

# This requires a single item or a tuple on the right. Format codes are modeled
# after the C printf() as well.

# Note: This is the ONLY FORMATTING available on byte strings

b'%s has %d messages' % (b'Dave', 37)

print(b'%b has %d messages' % (b'Dave', 37))

# Excercises
#
# Excercise 2.8: How to format numbers
#
# A common problem with printing numbers is specifying the number of decimal
# places. One way to fix this is to use f-strings. Try these examples:

value = 42863.1

print(value)

print(f'{value:0.4f}')

print(f'{value:>16.2f}')

print(f'{value:<16.2f}')

print(f'{value:*>16,.2f}')

# Formatting is also sometimes performed using the % operator of strings
#
print('%0.4f' % value)

print('%16.2f' % value)

# Although it's commonly used with print, string formatting is not tied
# to printing. If you want to save a formatted string, just assign it to
# a variable

f = '%0.4f' % value



