# Recursion is repeated application of the same procedure to a small problem
# It lets us tackle complex problems by reducing the problem to a simpler one

# A recursive function calls itself usually with a modified parameter until it reaches a specific condition. 
# That condition is called `base case`
def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n-1)

def factorial_(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)
factorial_(4)

# Why do we need recursive functions instead of just writing loops.

# Example: 
# You need to write a tool that goes through a bunch of directories 
# in your computer and calculates how many files are contained in each. 
# When listing the files inside a directory, you might find subdirectories inside them, 
# and you'd want to count the files in those subdirectories as well. 
#
# The base case would be a directory with no subdirectories. 
# For this case, the function would just return the amount of files. 



# Example 2: 
# Group of users that contains other groups
# - Active directory
# - LDAP

#for linter
def base_case_condition(parameters):
   return True
base_case_value = True
modified_parameters = True

#default
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)