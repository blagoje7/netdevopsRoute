# Data inside a `dictionary` takes a form of pair {`key` : `value`}
x = {}
type(x)

#Instead of series of slots with values we have series of keys pointing to values

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts) # its perfectly normal to mix types of values between keys and values

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["txt"]

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print("jpg" in file_counts) # true
print("html" in file_counts) # false

#dictionaries are muttable

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["cfg"] = 8 # adds new pair key : value
print(file_counts)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["csv"] = 17 # replaces value
print(file_counts)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23, 'cfg':8}
del file_counts["cfg"] # deletes pair key : value
print(file_counts)
