# concatenating works but its tricky to use for more complex transformations of strings
# we can use .format() for that kind of work
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number)) # we generate placeholders for variables with {} 
# after we pass variables to format() and they will be placed in placeholders in order they are passed to `format` method

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
# we can controll in what order variables appear in string, but we need to pass them in a slightly different way

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax)) # in this case there is formatin expression inside placeholders
# : separates expression from the field name we used in last example, this one means we are formating float number, hence f
# and that there are going to be 2 digits after decimal point .

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x))) # here we are using > to aling text to the right for a total of 3 spaces
  # in 2nd part we are saying " Aling to right for exactly 6 spaces, and have 2 digits after decimal point . "