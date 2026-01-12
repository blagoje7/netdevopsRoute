message = "A kong string with a silly typo"
# message[2] = "l"
# This will throw an error
# TypeError : strings do not support item assignemnt
# In other words strings in Python are immutable

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

message = "This is a new message"
print(message)
# But we can assign new value to variable
message = "And another one"
print(message)

pets="Cats & Dogs"
# we can use index() method to know index we want to change
# method is a function associated with certain class
pets.index("&")
pets.index("C")
# for longer substrings we ll get index where it is starting
pets.index("Dog")
pets.index("s")

pets="Cats & Dogs"
pets.index("x")
#This will throw an error, ValueError

pets="Cats & Dogs"
# with keyword in we can check if substring is contained inside of string we want to check
print("Dragons" in pets)
print("Cats" in pets)

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

# Some Basic string methods
animals = "lions tigers and bears"
animals.index("g")

animals = "lions tigers and bears"
animals.index("bears")

animals = "lions tigers and bears"
if "horses" in animals:
    print(animals.index("horses"))


