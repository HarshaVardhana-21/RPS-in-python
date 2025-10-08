import random

# computerChoice = random.choice(["Rock", "Paper","Scissors"])
# choices = {"Rock": -1, "Paper": 0,"Scissors": 1}
# yourDict = int(input(f"{choices} \nPick you choice: "))
# revChoices = {-1:"Rock",0:"Paper" ,1:"Scissors"}
# you= revChoices[yourDict]

# print(f"You choose {you} and computer choose {computerChoice}")

# if you == computerChoice:
#     print("It's a tie")
# elif (you == "Rock" and computerChoice == "Scissors") or (you == "Paper" and computerChoice == "Rock") or (you == "Scissors" and computerChoice == "Paper"):
#     print("You win")
# else:
#     print("Computer wins")
    
# Now write a program where the same code runs untill the user wants to exit.

while True:
    playAgain = input("Play Rock, Paper, Scissors? (y/n): ").strip().lower()
    if playAgain != 'y':
        print("Thanks for playing!")
        break

    computerChoice = random.choice(["Rock", "Paper","Scissors"])
    choices = {"Rock": -1, "Paper": 0,"Scissors": 1}
    yourDict = int(input(f"{choices} \nPick you choice: "))
    revChoices = {-1:"Rock",0:"Paper" ,1:"Scissors"}
    you= revChoices[yourDict]

    print(f"You choose {you} and computer choose {computerChoice}")

    if you == computerChoice:
        print("It's a tie")
    elif (you == "Rock" and computerChoice == "Scissors") or (you == "Paper" and computerChoice == "Rock") or (you == "Scissors" and computerChoice == "Paper"):
        print("You win")
    else:
        print("Computer wins")