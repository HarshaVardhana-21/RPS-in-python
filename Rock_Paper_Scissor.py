import random

computerChoice = random.choice(["Rock", "Paper","Scissors"])
choices = {"Rock": -1, "Paper": 0,"Scissors": 1}
yourDict = int(input(f"{choices} \nPick you choice: "))
revChoices = {-1:"Rock",0:"Paper" ,1:"Scissors"}
you= revChoices[yourDict]

print(f"You choose {you} and computer choose {computerChoice}")

if(you == computerChoice):
    print("It's a draw")
else:
    if(you == "Rock" and computerChoice == "Scissors"):
        print("You win !!!")
    elif(you == "Scissors" and computerChoice == "Rock"):
        print("Computer wins ..!")
        
    elif(you == "Scissors" and computerChoice == "Paper"):
        print("You win !!!")
    elif(you == "Paper" and computerChoice == "Scissors"):
        print("Computer wins ..!")
        
    elif(you == "Paper" and computerChoice == "Rock"):
        print("You win !!!")
    elif(you == "Rock" and computerChoice == "Paper"):
        print("Computer wins ..!")