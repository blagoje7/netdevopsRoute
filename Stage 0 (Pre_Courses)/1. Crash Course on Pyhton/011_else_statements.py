# It is possible to cover other possibilities of statment we are evaluating in if statment
# It is done with else statement, in previous example we would just skip execution of if statement if it was false
# Now we are doing other branch if it is false

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")

# Arithmetic operators
# any comparison returns either `True` or `False` which is perfect for if statements
# in this example we do not need else statement because only other possible branch in if statement is false so we can just return False
# this % is `moduo` operator, it returns remainder of division between two numbers
def is_even(number):
    if number % 2 == 0:
        return True
    return False

# In this case reaching return statement puts us out of function so, if remainder is 0 we reach return and nothing after in function is reachable, if it skips indented if part we reach return False and get out of the function

# The integer division is an operation between integers that yields two results, which are both integers, the quotient and the remainder. So if we do an integer division between 5 and 2, the quotient is 2 and the remainder is 1. 