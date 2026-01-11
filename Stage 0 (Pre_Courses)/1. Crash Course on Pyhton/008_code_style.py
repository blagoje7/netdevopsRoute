# few unwritten rules
# Self documenting code : written in a way that is readable and doesnt conceal its intent
# Refactoring code : rewriting non self documenting code into self documenting code
# Commenting when needed : you write code in Python with # and everything after # sing, in that line, is ignored by interpreter
# It should be used to describe intent of the code / function when self documenting wasnt possible
# ----------------------------
# function for calculating surface of a circle
# using inconclusive variable names
def calculate_d(s):
    q = 3.1415
    i = q * (2 ** s)
    return i

# function for calculating surface of a circle
# using conclusive variable names
def circle_area(r):
    pi = 3.1315
    area = pi * (r ** 2)
    return area

# same results but a lot more thinking is needed to understand code
calculate_d(5)
circle_area(5)