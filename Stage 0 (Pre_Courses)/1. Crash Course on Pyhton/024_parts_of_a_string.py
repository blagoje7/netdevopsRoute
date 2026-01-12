# String indexing
name = "Jaylen"
# Indexing, like in for loop start from 0
print(name[1])

name = "Jaylen"
print(name[0])

name = "Jaylen"
print(name[5])
# name[6] will throw IndexError : string index out of range
# We can only go to len() - 1
print(name[6])

# If we want to go to last character without knowing how long it is
text = "Random string with a lot of characters"
print(text[-1])
print(text[-2])

# Slice ( substrings )
color = "Orange"
# from first index to 2nd - 1
color[1:4]

fruit = "Pineapple"
# from first to 4th
print(fruit[:4])
# from 4th to last
print(fruit[4:])

fruit = "Mangosteen"
print(fruit[:5] + fruit[5:])
'Mangosteen'

# we can get index of specific char with .index() but it will print only first index that letter appears on 
print("systemy".index("y"))