# Branching is programs ability to alter its execution sequence

# The keyword, either def or if indicates the start of a special block. At the end of the first line, we use a colon, and then the body of the function or the if block is indent to the right. 
# The body of the if block will only execute when the condition evaluates to true. Otherwise, it's skipped. 
def hint_username(username):
    if len(username) < 3:
        print("Username must be at leat 3 characters long")

