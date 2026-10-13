from art import *
import random
from game_data import data
print(logo)
def format_data(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, {desc}, from {country}."
def answer(user_input,A_follower,B_follower):
    if A_follower > B_follower:
        return user_input=="A"
    else:
        return user_input=="B"
score = 0
cont=True
B=random.choice(data)
while cont:
    A=B
    B=random.choice(data)
    if A==B:
        B = random.choice(data)
    print(f"Compare A: {format_data(A)}")
    print(vs)
    print(f"Against B: {format_data(B)}")

    user_input=input("Who has more followers? Type 'A' or 'B': ").upper()
    print("\n"*20)
    print(logo)
    A_follower=A["follower_count"]
    B_follower=B["follower_count"]

    is_correct=answer(user_input,A_follower,B_follower)
    if is_correct:
        score+=1
        print(f"You're correct, your score is {score}")
    else:
        print(f"You're wrong, your final score is {score}")
        cont=False
