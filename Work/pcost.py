# pcost.py
#
# Excercise 1.27: Reading a data file
#
#Now that you know how to read a file, let us write a program to perform
#a simple calculation.
#
#The columns in portfolio.csv correspond to the stock name, number of shares,
#and purchase price of a single stock holding. Write a program called pcost.py
#that opens this file, reads all lines, and calculates how much it cost to purchase
#all of the shares in the portfolio.

# Hint: to convert a string to an integer, use int(s). To convert a string to a
# floating point, use float(s).

# Your program should print output such as the following:
# Total cost 44671.15

with open('Work/Data/portfolio.csv', 'rt') as f:
    next(f)
    sum = 0
    for line in f:
        row = line.split(',')
        _, n_shares, share_price = row
        sum = sum + int(n_shares) * float(share_price)
    print(f'Total cost {sum:.2f}')

