import random

def getuser_choice():
    user_choice = input("Pick Rock (R), Paper (P), or Scissors (S): ")
    return user_choice

def game():
    user_score = 0
    computer_score = 0
    while user_score < 3 and computer_score < 3:
        user_choice = getuser_choice()
        computer_choice = random.choice(['R', 'P', 'S'])

        print("Computer picked:", computer_choice)

        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 'R' and computer_choice == 'S') or \
             (user_choice == 'P' and computer_choice == 'R') or \
             (user_choice == 'S' and computer_choice == 'P'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print("Score: User", user_score, "- Computer", computer_score, "\n")

    if user_score >= 3:
        print(" You win the game!")
    else:
        print("Computer wins")
game()













