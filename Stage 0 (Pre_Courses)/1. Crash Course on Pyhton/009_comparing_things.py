# Basics
# results of comparisons are Boolean type, its a logical data type containing only 2 values "True" or "False"
print(10 > 1)
# True (greather then)
print("cat" == "dog")
# False (equal)
print(1 != 2)
# True (not equal)
#--------------
# errors
print(1 > "1")
#will return type error
print(1 == '1')
# False 
#--------------
# logical comparison
print("Yellow" > "Cyan" and "Brown" > "Magenta")
# False 
print("Yellow > Cyan")
print("Yellow" > "Cyan")
print("Brown > Magenta")
print("Brown" > "Magenta")
# strings are compared lexicographically, letter by letter by their unicode values, case-sensitive by default

print(25 > 50 or 1 != 2)
# True

print(not 42 == "Answer")
# True

# Integers
# ==    (equality) 
print(32 == 30+2)
print(5+10 == 6+7)

# !=     (not equal to) 
print(10-4 != 10+4)
print(9/3 != 3*1)

# >       (greater than)
print(11 > 3*3)
print(4/2 > 8-4) 

# <      (less than)
print(4/2 < 8-4)
print(11 < 3*3)

# >=    (greater than or equal to)
print(12*2 >= 24)
print(18/2 >= 15)

# <=    (less than or equal to)
print(12*2 <= 30)
print(15 <= 18/2)

# Strings
# == 
# The == operator can check if two strings are equal to each other. 
# If they are equal, the Python interpreter returns a True result.
print("a string" == "a string")
print("4 + 5" == 4 + 5)
print("three" == 3)

# !=
event_city = "Shanghai"
print(event_city != "Shanghai")
print("rabbit" != "frog")

# < , > 
# The comparison operators greater than > and less than < can be used to alphabetize words in Python. The letters of the alphabet have numeric codes in Unicode (also known as ASCII values). The uppercase letters A to Z are represented by the Unicode values 65 to 90. The lowercase letters a to z are represented by the Unicode values 97 to 122. 

print("Wednesday" > "Friday")
print("Brown" < "brown")
print("sunbathe" > "suntan")

# <= , >=

var1 = "my computer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"
 
print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" less than or equal to \"pineapple\"? Result: ", var3)

# Logical operators
# and
#Both sides of the statement being evaluated must be True for the whole statement to be True. 
print(5 > 1 and 5 < 10)
print((6*3 >= 18) and (9+9 <= 36/2))
print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")
#------------------
# or
# If either side of the comparison is True, then the whole statement is True. 
print(5>1 or 1>5)

# Define country and city variables
country = "United States"
city = "New York City"
# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))  # True or True = True
# False or True returns True
print(country == "New York City" or city == "New York City")  # False or True = True
# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)  # True or False = True
# False or False returns False
print("B_name" > "C_name" or "B_name" < "A_name") # False or False = False
#----------------
# not
# Inverts the Boolean result of the statement immediately following it. So, if a statement evaluates to True, and we put the not operator in front of it, it would become False. 
print(not 5>1)

x = 2*3 > 6
print("The value of x is:")
print(x)
print("")  # Prints a blank line
print("The inverse value of x is:")
print(not x)

today = "Monday"
print(not today == "Tuesday") 
# The "today" variable states today is Monday. This makes the comparison
# "today == Tuesday" False. The logical operator "not" inverts the False
# result to become True.