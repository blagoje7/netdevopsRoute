multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)

# because creating list from loops is very common task Python provides us with
multiples = [x*7 for x in range(1,11)] # List comperhensions, it lets us create new lists based on sequences or range
print(multiples)


languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)


z = [x for x in range(0,100+1) if x % 3 == 0]
print(z)

# When to use for loop vs when to use list comperhension

# For loop iterates over a sequence of values
# For more complrex ideas its probably better to use for loop

# List comperhension lets us create new list baed on sequences or ranges
# If it can make it in single line its probably list comperhension time

# Questions to ask.
# Which one makes my code more clear and consise?
# Which one makes my code more readable and understandable to other people?