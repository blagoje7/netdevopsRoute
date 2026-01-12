# len(string) - Returns the length of the string
print(len("abcde"))         # prints 5

# for character in string - Iterates over each character in the string
for c in "abcde":
    print(c)      # prints "a", then "b", then "c", etc.

# if substring in string - Checks whether the substring is part of the string
print("abc" in "abcde")     # prints True
print("def" in "abcde")      # prints False

# string[i] - Accesses the character at index i of the string, starting at zero
print("abcde"[2])           # prints "c"
print("abcde"[-1])          # prints "e"

# string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted, its value defaults to 0. If j is omitted, Python returns everything from i to the end of the string.
print("abcde"[0:2])        # prints "ab"
print("abcde"[2:])          # prints "cde"

# String methods
#string.lower() - Returns a copy of the string with all lowercase characters
print("AaBbCcDdEe".lower())             # prints "aabbccddee"
# string.upper() - Returns a copy of the string with all uppercase characters
print("AaBbCcDdEe".upper())             # prints "AABBCCDDEE"

# string.lstrip() - Returns a copy of the string with the left-side whitespace removed
print("      Hello    ".lstrip())           # prints "Hello   "
# string.rstrip() - Returns a copy of the string with the right-side whitespace removed
print("    Hello  ".rstrip())               # prints "   Hello"
# string.strip() - Returns a copy of the string with both the left and right-side whitespace removed
print("     Hello     ".strip())                # prints "Hello"

# string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.
print("12345".isnumeric())              # prints True
print("-123.45".isnumeric())            # prints False

# string.isalpha() - Returns True if there are only letters in the string. If not, returns False.
print("xyzzy".isalpha())                    # prints True

# string.count(substring)- Returns the number of times substring is present in the string
test = "How much wood would a woodchuck chuck"
print(test.count("wood"))               # prints 2

# string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)
test = "How much wood would w woodchuck chuck"
print(test.split())                 # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']

# string.split(delimiter) - Returns a list of substrings that were separated by whitespace or another string
test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))              # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']

# string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.
print(test.replace("wood", "plastic"))      # prints "How much plastic would a plasticchuck chuck"

# delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter
print("-".join(test.split()))            # prints "How-much-wood-would-a-woodchuck-chuck"