"Mountains".upper() # Brings all characters to upper case
"Mountains".lower() # - || - to lower case

answer = "YES"
if answer.lower() == "yes":
  print("User said yes")


" yes ".strip() # removes all spaces, tabs and inline characters. they are called whitespaces alltogether

" yes ".strip()
" yes ".lstrip() # we can also use it to remove whitespaces to the left
" yes ".rstrip() # or to the right

"The number of times e occurs in this string is 4".count("e") # how many times substrings appears in string

"Forest".endswith("rest")

"Forest".isnumeric() # false
"12345".isnumeric() # true

print(int("12345") + int("54321")) # when it is true we can bring string to actual number 

print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])) # called on a string that we will use to join
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))

print("This is another example".split()) # This will make list of strings out of sentence 