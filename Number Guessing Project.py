import random
from art import logo
computer_choice=random.randint(1,100)
def check_answer(user_guess,computer_choice):
    if user_guess>computer_choice:
        print("Too high.")
    elif user_guess<computer_choice:
        print("Too low.")
    else:
        print(f"You guessed the number and the answer was {computer_choice}.")
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
mode=input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
guess=True
if mode=="easy":
    attempts = 10
    print(f"You have {attempts} remaining to guess the number.")
    user_guess=int(input("Make a guess."))
    if user_guess==computer_choice:
        print("You guessed the number.")
    else:
        while guess==False:
            check_answer(user_guess,computer_choice)
            print("Guess again.")
            attempts=attempts - 1
            print(f"You have {attempts} remaining to guess the number.")
            if attempts < 1:
                print("You lose.")
                break
            user_guess = int(input("Make a guess."))
else:
    attempts = 5
    print(f"You have {attempts} remaining to guess the number.")
    user_guess = int(input("Make a guess."))
    if user_guess == computer_choice:
        print("You guessed the number.")
    else:
        while guess == False:
            check_answer(user_guess, computer_choice)
            print("Guess again.")
            attempts = attempts - 1
            print(f"You have {attempts} remaining to guess the number.")
            if attempts < 1:
                print("You lose.")
                break
            user_guess = int(input("Make a guess."))
