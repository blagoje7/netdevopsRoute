# for loop iterates over a sequence of values
for x in range(5):
# in Python range will start at 0 by default
# The list of a number generated will be one less then a given value
    print(x)

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value

print("Total sum: " + str(sum) + " - Average: " + str(sum/len(values)))

# General rule of thumb:
# Use for loops when there is sequence of elements you want to iterate 
# Use while loop when you want to repeat a task untill condition changes