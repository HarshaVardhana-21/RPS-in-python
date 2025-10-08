import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_user_choice():
    choices = {"Rock": -1, "Paper": 0, "Scissors": 1}
    yourDict = int(input(f"{choices} \nPick you choice: "))
    revChoices = {-1: "Rock", 0: "Paper", 1: "Scissors"}
    return revChoices[yourDict]

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie"
    elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
        return "You win"
    else:
        return "Computer wins"
    
while True:
    playAgain = input("Play Rock, Paper, Scissors? (y/n): ").strip().lower()
    if playAgain != 'y':
        print("Thanks for playing!")
        break

    computerChoice = get_computer_choice()
    userChoice = get_user_choice()

    print(f"You choose {userChoice} and computer choose {computerChoice}")
    result = determine_winner(userChoice, computerChoice)
    print(result)