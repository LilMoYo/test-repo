import random
total = 0
die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1 + die2

while total != 2:
  print("Nope")
  print("rerolling ...")
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  total = die1 + die2
  
  print("Die 1: " + str(die1))
  print("Die 2: " + str(die2))
  print("Total: " + str(total))
print("Snake eyes!")