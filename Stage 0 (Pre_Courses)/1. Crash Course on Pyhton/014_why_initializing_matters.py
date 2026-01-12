while my_variable > 10:
    print("Hello")
    my_variable += 1
# We "fooled" linter to think we initilized my_variable but when interpreter tries to read my_variable first time it does not exist

my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1


x = 1
sum = 0
while x < 10:
    sum += x
    x += 1
print(sum)

# x stays 10 after the loop so it will not do any iterations for next loop if we use it again without reseting value
# ie. even first check will fail because 10 = 10
product = 1
while x < 10:
    product *= x
    x += 1
print(product)

# Whenever writing the loop, check that you initialized all the variables you intend to use.