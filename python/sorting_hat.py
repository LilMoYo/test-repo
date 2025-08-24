
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

shat_q1 = int(input("Do you like Dawn or Dusk? \n 1) Dawn\n 2) Dusk\n Answer: "))

if shat_q1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif shat_q1 == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print("Wrong input.")

shat_q2 = int(input("When I'm dead, I want people to remember me as: \n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n Answer: "))
if shat_q2 == 1:
  hufflepuff = hufflepuff + 2
elif shat_q2 == 2:
  slytherin = slytherin + 2
elif shat_q2 == 3:
  ravenclaw = ravenclaw + 2
elif shat_q2 == 4:
  gryffindor = gryffindor + 2
else:
  print("Wrong input.")

shat_q3 = int(input("Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n Answer: "))
if shat_q3 == 1:
  slytherin = slytherin + 4
elif shat_q3 == 2:
  hufflepuff = hufflepuff + 4
elif shat_q3 == 3:
  ravenclaw = ravenclaw + 4
elif shat_q3 == 4:
  gryffindor = gryffindor + 4
else:
  print("Wrong input.")

print("--------------------")
print("Gryffindor: " + str(gryffindor))
print("Ravenclaw: " + str(ravenclaw))
print("Hufflepuff: " + str(hufflepuff))
print("Slytherin: " + str(slytherin))
print("--------------------")
max_housescore = max((gryffindor, "Gryffindor"), (ravenclaw, "Ravenclaw"), (hufflepuff,"Hufflepuff"), (slytherin, "Slytherin"))
print("")
print("Highest Housescore:")
print(max_housescore[1] + ": " + str(max_housescore[0]))
