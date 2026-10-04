rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images=[rock, paper, scissors]
choice=['rock', 'paper', 'scissors']
while True:
    print("What do you choose?")
    inp=int(input("Type 0 for Rock,1 for Paper or 2 for Scissors:"))
    comp = random.randint(0, 2)
    print("You chose:",game_images[inp])
    print("computer choose:",game_images[comp])
    if inp==comp:
        print("Draw")
    elif inp==0 and comp==2:
        print("you win")
    elif inp==1 and comp==0:
        print("you win")
    elif inp==2 and comp==1:
        print("you win")
    else:
        print("you lose")