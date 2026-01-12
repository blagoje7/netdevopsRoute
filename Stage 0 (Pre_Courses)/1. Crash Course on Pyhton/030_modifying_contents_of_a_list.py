# Lists are mutable
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi") # adds a new element at last index, it always adds to end no matter how long is the list
print(fruits)


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange") # if we want to add somwehere in the list
print(fruits)


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach") # it will not place it at index = 25 rather it will just add it to end of the list
print(fruits[5])
print(fruits)


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon") # remove() removes only first occurance of element we passed to it 
print(fruits)


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
# fruits.remove("Pear")
#This will throw an error, because there is no `Pear` inside the list 


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3) # accepts index and removes item at that index 
print(fruits)


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3) 
fruits[2] = "Strawberry"
print(fruits)
fruits.pop(0)
fruits.pop(0)
fruits.pop(0)
fruits.pop(0)
print(fruits)

# no matter how much we changed the list its always same variable, even when empty now

# Whenever we are going to use variable with variable amount of elements we are going to use a list