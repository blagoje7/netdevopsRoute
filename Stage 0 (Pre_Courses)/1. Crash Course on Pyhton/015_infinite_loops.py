x = 0
while x % 2 == 0:
    x = x / 2
#No output

if x != 0:
    while x % 2 == 0:
        x = x / 2
#No output

while x != 0 and x % 2 == 0:
    x = x / 2
#No output

def do_something_cool():
    return True

def user_requested_to_stop():
    return False

while True:
    do_something_cool()
    if user_requested_to_stop():
        break

# The body of the while loop needs to make sure that the condition being checked will change. 
# Or we get `infinite loops` a loop that keeps executing and never stops

# In Python we use keyword `break` to exit out of infiite loops if we intended to make them