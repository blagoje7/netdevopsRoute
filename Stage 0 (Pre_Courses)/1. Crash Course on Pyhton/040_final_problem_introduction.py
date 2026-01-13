# can make the work we do in our IT jobs faster and more efficient.
# To start solving our problem, we'll first look at the problem statement, 
# where we'll get an understanding of what we need to do and the inputs and
# outputs for the script we'll need to write. 

# We'll think about how we can tackle the problem with the tools already baked into Python. 
# Remember that we always want to avoid reinventing the wheel. #

# Once we know what we need to write and what we can use it to do, 
# we'll do some planning 


# Imagine you are IT specialist at medium sized company 
# Your manager wants to create daily report that tracks use of machines, 
# specifically manager wants to know whics users are currently connected to which machines.

# Its your job to create the report.

# In your company there's a system that collects every event that happens on the machines on the network.
# It collects each time user logs in and out of a computer

# With this information we want to create a script that generates a report of which user is logged into which machine at that time.

# Before writing a script we need to know: 
#       Which information we ll use as an input
#       Which information we ll have as an output

# Input

# In a scenario input is a list of events, Each event is an instance of the class
# Each event is an instance of the event class.
# An event class contains:
#  the date when the event happened             |date
#  the name of the machine where it happened    |machine
#  the user involved                            |user
#  and the event type                           |type

# all event types are strings
# Our script will receive a list of event objects and will access the events atributes

# Output 
# We want to generate a report that lists all the machine names, and for 
# each machine lists the users that are currently logged in.
# We then want this information printed on the screen.


