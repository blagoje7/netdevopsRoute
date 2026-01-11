#from our earlier example where we calculated area of the triangle, it was pretty simple
#base*height/2, but if we need to calculate this multiple times in multiple places in our code
#it would be useful that we can just call function and pass it base and height and get area back
#for that we need to `return` value from function (in line 6)
def area_triangle(base, height):
    return base*height/2
#value returnd like this needs to be stored in a variable, for each call of the function
area_a = area_triangle(6,2)
area_b = area_triangle(8,3)
sum = area_a + area_b
print("The sum of both areas is:", str(sum))

#we can even return more values from the functions
# // is used for floor (dividing integers)
def convert_seconds(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours*3600 - minutes*60
    return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(5481)
print(hours, minutes, seconds)

#trying to store value in variable from a function that doesnt have return statement gives us data type  `None`
#special data type in Python used to indicate that things are empty or that they returned nothing
def greeting(name):
    print("Welcome", name)
result = greeting("Blagoje")
print(result)

