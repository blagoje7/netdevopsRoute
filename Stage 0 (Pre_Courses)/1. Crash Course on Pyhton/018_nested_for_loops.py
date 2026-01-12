# Sometimes we need to run for loop inside for loop, like in example of printing all dominos without repeating so we would go into first side then print all dominos with that number on the left, and after we are finished we would just go into next number on the left and print all dominos in that row
for left in range(7):
  for right in range(left, 7):
    #end is special parameter that print is finishing with, by default its \n ( new row character )
    print("[" + str(left) + "|" + str(right) + "]", end=" | ")
  print()

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)


# Let's say your manager asks you to do an operation that goes through 10,000 elements and each takes 0.1 sec, thats pretty fast its 10 seconds, but adding nested loop for new 10,000 elements pushes that number to 100,000 seconds ( around 27 hours)
# It just tells us that we need to be careful where we use nested loops, they are useful but not everywhere
for element1 in long_list:
  for element2 in long_list:
    do_something(element1, element2)