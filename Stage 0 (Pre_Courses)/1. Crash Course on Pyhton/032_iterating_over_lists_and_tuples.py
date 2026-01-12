animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))


winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):    # much more logical in python, indexes are for strings mainly 
  print("{} - {}".format(index + 1, person))    # in python its much more idiomatic to access elements directly, or to use enumerate
# for example when we are modiflying elements of the lists we are indexing

# CAUTION: You need to be extra careful when iterating and modifying list at the same time

def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))


# Example of enumerate

def skip_elements(elements):
	# code goes here
	result = []
	for index, element in enumerate(elements):
		if index % 2 ==0:
			result.append(element)
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']