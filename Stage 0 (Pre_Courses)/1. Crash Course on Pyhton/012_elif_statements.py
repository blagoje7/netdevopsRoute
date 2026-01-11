# `elif` is short from `else if`
# Main difference with `if` and `elif` blocks is that `elif` block can only be used as companion to `if` block
# Because condition of `elif` statement will only be checked if condition of `if` statement wasnt true
# There is no limit how many `elif` condition there can be

def hint_password(password):
    if len(password) < 3:
        print("Password must be at least 3 characters long")
    elif len(password) > 15:
        print("Password must be less then 15 characters long")
    else:
        print("Valid password")
