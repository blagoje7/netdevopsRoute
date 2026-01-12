greeting = "Hello"
for c in greeting:
    print(f'Next character in {greeting} is {c}')

# You can use for loops with strings to perform tasks and functions such as:
#   Reading text from a file
#   Searching for a value or specific data in a document or spreadsheet 

# Looping over a string

#printing position of characters in string with for loop
greeting = 'Hello'
for i in range(len(greeting)):
	print("On position", i, "is", greeting[i], "character")
      
# with while loop    
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1

# with while loop and string slicing
greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index:index+1])
    index += 1

# List comperhensions 
# a concise way to create lists in Python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)