# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters and
# each time it hits the ground, it bounces back up to 3/5
# the height it fell. Write a program bounce.py that prints
# a table showing the height of the first 10 bounces.

counter = 0
ball_height = 100
bounce_height = 0

while counter < 10:
    bounce_height = 3/5 * (ball_height)
    ball_height = bounce_height
    print(counter + 1, round(bounce_height, 4))
    counter +=1

