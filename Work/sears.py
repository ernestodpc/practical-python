# Excercise 1.6: Debugging
# The following code fragment contains code from the Sears tower problem.
# it also has a bug in it.

bill_thickness = 0.11 * 0.001 #Meters (0.11mm)
sears_height   = 442          #Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
