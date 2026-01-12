# or x in 25:
#   print(x)
#this will produce an error

for x in range(25):
    print(x)
#this will make the error go away

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends("Barry")
greet_friends(["Barry"])
# This happens because strings are iterable, we need to create list even if there is only one element

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])