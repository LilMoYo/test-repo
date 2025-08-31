import random
player = ""
computer = random.randint(1,5)

p1 = "The player won!"
c1 = "The computer won!"
in_msg = "Enter the number of your move: "

rps = ["0", "✊", "✋", "✌️", "🦎", "🖖"]

print("Which move would you like to use?")
print("1) ✊ (Rock)")
print("2) ✋ (Paper)")
print("3) ✌️ (Scissors)")
print("4) 🦎 (Lizard)")
print("5) 🖖 (Spock)")

while not player.isdecimal():
    try:
        player = input(in_msg)
    except ValueError:
        print("Please use a number!")
        player = input(in_msg)
      
player_int = int(player)

while player_int == 0 or player_int > 5:
    player_int = int(input(in_msg))

print(f"You chose: {rps[player_int]}")
print(f"Computer chose: {rps[computer]}")

## Rock ##
if player_int == 1 and computer == 3:
    print(p1)
elif player_int == 1 and computer == 4:
    print(p1)

## Paper ##
elif player_int == 2 and computer == 1:
    print(p1)
elif player_int == 2 and computer == 5:
    print(p1)

## Scissors ##
elif player_int == 3 and computer == 2:
    print(p1)
elif player_int == 3 and computer == 4:
    print(p1)
    
## Lizard ##
elif player_int == 4 and computer == 2:
    print(p1)
elif player_int == 4 and computer == 5:
    print(p1)

## Spock ##
elif player_int == 5 and computer == 1:
    print(p1)
elif player_int == 5 and computer == 3:
    print(p1)
    
## Tie ##
elif player_int == computer:
    print("Tie!")

## Computer wins ##
else:
    print(c1)