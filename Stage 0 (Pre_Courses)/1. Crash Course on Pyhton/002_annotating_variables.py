#Dynamic typing
a = 3       #a is an integer
b = 'Hello world'

#it allows programmers to write programs quickly and offers flexiblility
#Note: Pyhton decides what type variable is and how it should behave.

#Annotating with type comments
c = 3       #type : int
d = '3'     #type : str

#interpreter will ignore these comments so its only for people reading code

#Annotating directly ("Modern way")
e : str = '3'
f : str = 3

#its still not rule!
print(f)
#this will work but if you want to catch errors like this while you code you need to use linter (Pylance or MyPy)

#Pro tip : being strategic with annotating variables directly because it can add unnecesary overheard when overused.
#its less common when doing data science (it can be almost imposible to manually map data every time new set arives) but very useful when dealing with OOP problems


