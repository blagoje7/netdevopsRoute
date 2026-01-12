# In last example we had couple of [ ] next to strings
# Its called `bracket notation`
# used to specify the start of the index, ending index, or both. If you do not include the starting index, then the slice contains everything from the beginning of the string to the ending index. This is the same if you do not include the ending index.
string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”

# If your index is negative, Python counts back from the end of the string instead of the beginning.
print(string1[-10:0])

# If your index is beyond the end of the string, Python returns an empty string.
print(string1[55:])

# But not same with negative index out of range
print(string1[-50:])

# Stride
# An optional way to slice an index is by the stride argument, indicated by using a double colon. 
# Something like step in for loop
# Using a negative stride, the string prints backwards.

# Prints “Getns atlns”
print(string1[0::2])

# Prints “sgnilhtraE ,sgniteerG”
print(string1[::-1])


# How to join strings

# Most common way, already used
# Prints “Hello world”
print("Hello" + " " + "world")

# join() can also be used
greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"

# You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!")  # Prints "Hello, Alice!"

# How to combine slicing and joining strings

phonenum = '2025551212'
# The first 3 digits are the area code:
area_code = "(" + phonenum[:3] + ")"
# The next 3 digits are called the “exchange”:
exchange = phonenum[3:6]
# The last 4 digits are the line number:
line = phonenum[-4:]
# Put the pieces back together into a nicely formatted string:
joinednumber = area_code + " " + exchange + "-" + line

# If we create function out of this
def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

print(format_phone('2025551212'))


# append()
sequence = range(10)
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)

sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]

# print * 8 times
print("*" * 8)