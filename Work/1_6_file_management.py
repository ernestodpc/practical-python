#Section 1.6 File Management

#Excercises: These excercises depend on a file "Data/porfolio.csv". The file
#contains a list of lines with information on a porfolio of stocks. It is
#assumed that you are working in the practical-python/Work directory. If
#you are not sure, you can find out where Python thinks it's running by
#doing this:
#
import os

os.getcwd()

#Excercise 1.26: File preliminaries
#First try reading the entire file all at once as a big string

with open('Work/Data/portfolio.csv', 'rt') as f:
    data = f.read()

print(data)

with open('Work/Data/portfolio.csv', 'rt') as f:
    for line in f:
        print(line, end='')

f = open('Work/Data/portfolio.csv', 'rt')

type(f)

headers = next(f)

headers

for line in f:
    print(line, end='')

f.close()

f = open('Work/Data/portfolio.csv', 'rt')
headers = next(f).split(',')
headers

for line in f:
    row = line.split(',')
    print(row)

f.close()

# Excercise 1.28: Other kinds of files
#
# What if you wanted to read a non-text file such as a gzip-compressed datafile?
# The builtin open() function won't help you here, but Python has a library module
# gzip that can read gzip compressed files.
# Try it:

import gzip

with gzip.open('Work/Data/portfolio.csv.gz', 'rt') as file:
    for line in file:
        print(line, end='')

# Note: Including the file mode of 'rt' is critcal here. If you forget that,
# you'll get byte strings instead of normal text strings.

# Commentary: Shouldn't we being using Pandas for this?
#
# Data scientists are quick to point out that libraries like Pandas already have
# a function for reading CSV files. This is true-and it works pretty well. However,
# this is not a course on learning Pandas.
# Reading files is a more general problem than the specifics of CSV files. The main
# reason we're working with a CSV file is that it's a familiar format to most coders
# and it's relatively easy to work with directly illustrating many Python features in
# the process. So, by all means use Pandas when you go back to work. For the rest of
# this course however, we're going to stick with standard Python functionality.

