import random
computer = random.randint(1,3)

p1 = "The player won!"
c1 = "The computer won!"

rps = ["0", "✊", "✋", "✌️"]

print("Which move would you like to use?")
print("1) ✊ (Rock)")
print("2) ✋ (Paper)")
print("3) ✌️ (Scissors)")
player = int(input("Enter the number of your move: "))

print(f"You chose: {rps[player]}")
print(f"Computer chose: {rps[computer]}")

if player == 1 and computer == 3:
    print(p1)
elif player == 2 and computer == 1:
    print(p1)
elif player == 3 and computer == 2:
    print(p1)
elif player == computer:
    print("Tie!")
else:
    print(c1)