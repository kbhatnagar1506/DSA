import random
human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(type(human))
computer=random.randint(0,2)
print(f"Computer chose:{computer}")

if human == 0 and computer == 1:
     print("You lose")
elif human == 0 and computer == 2:
     print("You win")
elif human == 1 and computer == 0:
     print("You win")
elif human == 1 and computer==2:
     print("You lose")
elif human == 2 and computer == 0:
     print("You lose")
elif human == 2 and computer == 1:
     print("You win")
else:
     print("draw")

