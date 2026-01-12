# Lists are like long boxes dividied in different slots, each contains different value, and each with its own index
# We are using [] to indicate where list starts and ends
x = ["Now", "we", "are", "cooking!"]


x = ["Now", "we", "are", "cooking!"]
type(x) # Python tells us type is `list`


x = ["Now", "we", "are", "cooking!"]
print(x)    # prints whole list of items


x = ["Now", "we", "are", "cooking!"]
len(x)


x = ["Now", "we", "are", "cooking!"]
print("are" in x)


x = ["Now", "we", "are", "cooking!"]
print("Today" in x)


x = ["Now", "we", "are", "cooking!"]
print(x[0])
print(x[3])


x = ["Now", "we", "are", "cooking!"]
#print(x[4])
#This last line will throw an error. IndexError

# we can also slice lists
x = ["Now", "we", "are", "cooking!"]
x[1:3]


x = ["Now", "we", "are", "cooking!"]
x[:2]


x = ["Now", "we", "are", "cooking!"]
x[2:]

#String and Lists are both examples of Sequences
# all sequences share:
# for element in sequence
# sequence[x]
# len(sequence)
# sequence + sequence - concatenateion
# element in sequence