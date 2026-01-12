# Sometimes we do not want to start at 0, for this examples range gives us option of starting with different numbers
product = 1
for n in range(1,10):
  product = product * n

print(product)

# Additionally, we can specify a third parameter to change the size of each step. This means that instead of going one by one, we could have a larger difference between the elements. 
def to_celsius(x):
  return (x-32)*5/9

print("F", "   C")
for x in range(0,101,10):
  print(x, round(to_celsius(x),2))

# Closer look at `range()`

# For example, if you have a loop with the range: for n in range(1, 5, 6), the range will only produce the numeric value 1. This is because the incremental value of 6 exceeded the ending point of the range.
print(range(1, 5, 6))

x = 1
y = 1
z = 1
for n in range(x, y, z):
    print(n)

# This loop iterates on the value of the "x" variable in a range
# of 2 to -1 (the end-of-range index -2 is excluded). The third 
# parameter is also a negative number, making it a decremental value
# of -1. The print() function will output the resulting value of
# "x" as it starts at 2 and counts down to -1 (index -2).


for x in range(2, -2, -1):
    print(x)