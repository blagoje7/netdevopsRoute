file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts: # possible to use for loops to iterate throught a dict
  print(extension) # prints all keys
# EACH KEY CAN ONLY BE PRESENT ONCE

# you can either use the keys as indexes of 
# the dictionary or you can use the items method, 
# which returns a tuple for each element in the dictionary. 
# The tuples first element is the key, its second element is the value. 

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items(): # first variable is key , 2nd is value
  print(f"There are {amount} files with the .{ext} extension") 

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts.keys() # just keys
file_counts.values() # just values


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for value in file_counts.values(): # iterate through values
  print(value)

# EACH KEY CAN ONLY BE PRESENT ONCE

def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result
count_letters("aaaaa")
count_letters("tenant")
count_letters("a long string with a lot of letters")