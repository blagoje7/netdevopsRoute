# each time we want to perform calculation we change value of the variables and write the formula
# then print the greeting followed by the lucky number
# When you find things that are repeating its good idea to see if you can create a function to clean things up a bit 
name = "Kay"
number = len(name)*9

print("Hello", name, "your lucky number is ", str(number))

name = "John"
number = len(name)*9

print("Hello", name, "your lucky number is", str(number))

# updated script gives us same result but looks a lot cleaner and is infinitly times more reusable
def lucky_number(name):
    number = len(name)*9
    print("From fun `lucky_number(name)` : Hello", name, "your lucky number is", str(number))

lucky_number("Kay")
lucky_number("John")