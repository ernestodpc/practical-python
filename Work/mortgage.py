# mortgage.py
#
# Exercise 1.7
# Dave's mortgage
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000
# with Guido's Mortgage, Stock investment, and Bitcoin trading corporation.
# The interest rate is 5% and the monthly payment is $2684.11.

# Here's a program that calculates the total amount that Dave will have
# to pay over the life of the mortgage: ---> Completed

# Excercise 1.8
# Suppose Dave pays an extra $1000/month for the first 12 months of the
# mortgage.  Modify the program to incorporate this extra payment and
# have it print the total amount paid along with the number of months
# required.

# When you run the new program, it should report a total payment of
# $929_965.62 over 342 months. ---> Completed

# Excersice 1.9: Making an Extra Payment Calculator
#
# Modify the program so that the extra payment information can be more
# generally handled. Make it so that the user can set these variables:
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000.0

# Make the program look at these variables and calculate the total paid
# appropriately.

# How much will Dave pay if he pays an extra 1000/month for 4 years starting
# after the first five years have already been paid?

# Excercise 1.10: Making a table
#
# Modify the program to print out a table showing the month, total paid so far,
# and the remaining principal. The output should look something like this:

# Excercise 1.11: Bonus
# While you're at it, fix the program to correct for the overpayment that
# occurs in the last month


principal = 500_000.0
rate = 0.05
base_payment = 2684.11
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0
elapsed_months = 0

while principal > 0:
    elapsed_months += 1
    if elapsed_months >= extra_payment_start_month and elapsed_months <= extra_payment_end_month:
        payment = base_payment + extra_payment
    else:
        payment = base_payment
    if principal < payment and principal > 0:
        payment = principal
        principal = 0
    else:
        principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
    print(f'{elapsed_months: >10}', f'{round(total_paid,2): >5.2f}', f'{round(principal,2): >5.2f}')

print('Total paid: ', round(total_paid, 1))
print('Months: ', elapsed_months)
