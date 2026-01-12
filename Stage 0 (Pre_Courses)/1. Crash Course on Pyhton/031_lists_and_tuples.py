# tuples are sequences of elemets that are immutable
# if we have need for lists that always have certain element at certain place
# positions of an element inside a tuple have meaning
fullname = ('Grace', 'M', 'Hopper')

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds # this function returns a tuple
result = convert_seconds(5000)
type(result) # we see that result is tuple


def convert_seconds_(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
print(result)


def convert_seconds__(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
hours, minutes, seconds = result # we can unpack tuples, and because its immutable we know meaning wont change
print(hours, minutes, seconds)


def convert_seconds___(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(1000) # we can even unpack straight from the function
print(hours, minutes, seconds)
