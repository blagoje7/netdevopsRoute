# While loops instruct your computer to continuously execute your code based on your condition
# Initializing - Giving initial value to a variable

# A while loop will continuously execute code depending on the value of a condition. It begins with the keyword while, followed by a comparison to be evaluated, then a colon. On the next line is the code block to be executed, indented to the right. 
# Once the statement is no longer true, the loop exits and the next line of code will be executed.  

x = 0
while x < 5:
    print("Not there yet, x=", str(x))
    x = x + 1
print("x=",str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt", str(x))
        x+=1
    print("Done")

attempts(5)

#dummy for errors
def get_username():
    return 1
#dummy for errors
def valid_username(username):
    return False

# while not!
username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()

# Again important thing to mention is that, same as in `if` statement expression that we are checking while for needs to evaluate to either true or false