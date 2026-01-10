#functions are part of code that can easily be reusable
#To define a function, we use the def keyword. 
#The name of the function is what comes after the keyword. 
#--------------------------
#Simple function of greeting person whose name is entered in function
#In this example, the function's name is greeting. 
#So to call the function later in the script, we'll simply use greeting()

def greeting(name):
    #After the colon, we have the body of the function. That's where we state what we want our function to do. Note how the body is indented to the right. This is a key characteristic of Python
    #Each line inside the function must be indented same number of spaces to the right, we are using 4 spaces (because its how many spaces tab is) but we can use any number of spaces as long as it is consistent
    print("Welcome, " + name)
    
greeting("Kay")
greeting("Cameron")

#--------------------------

def greeting2(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)
    
greeting2("Blake", "Python crash course")
greeting2("Ellis", "Python crash course")

#--------------------------

