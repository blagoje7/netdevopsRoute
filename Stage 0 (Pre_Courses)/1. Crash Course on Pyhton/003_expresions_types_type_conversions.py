a = 8
b = a+8.5
print(type(a))
print(type(b))
#it allowed to add ints and float but it will automatically change type of int to float 
#that conversion is called 'Implicit conversion' meaning interpretor automatically converts it 

print("a" + "b" + "c")
print("This" " concat" + " feature" + " is" + " pretty" + " neat!")
#simple concat

base = 6
height = 8
area = base*height/2
print("For triangle with base = " + str(base) + " and height = " +  str(height) + " area is " + str(area))
print(f"It can be writen in a different way with `f strings` : For triangle with base = {base} and height = {height} area is {area}")
print(f"In f strings you can do math right inside print or other function giving you that for that specific triangle area is {base*height/2}")

# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests

#---------------------------------------------------------------------

# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type

#---------------------------------------------------------------------

#In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function to convert the number into a string. 

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))

#---------------------------------------------------------------------

# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.

#---------------------------------------------------------------------

# The following code causes a type error between a string 
# and an integer:

#print("5 * 3 = " + (5*3)) 


# Resolution: 
print("5 * 3 = " + str(5*3))

#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.  

#---------------------------------------------------------------------

numerator = 7
denominator = 0   # Possible resolution: Change the denominator value 
result = numerator / denominator
print(result)


# One possible assumption for a number divided by zero error might
# include the issue of a null value as a denominator (could happen when
# using a loop to iterate over values in a database). In such cases, the
# desired outcome may be to leave the numerator value intact. The
# numerator value can be preserved by reassigning the denominator with 
# the integer value of 1. The result would then equal the numerator.