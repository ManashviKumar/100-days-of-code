from turtle import Turtle,Screen
import random
race_on=False
screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will you choose?")
colors=["red","green","blue","yellow","violet","indigo","orange"]
y_pos=[-70,-40,-10,20,50,80,110]
turtles=[]
for index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-238, y=y_pos[index])
    turtles.append(new_turtle)

if user_bet:
    race_on=True
while race_on:

    for turtle in turtles:
        if turtle.xcor()>230:
            race_on=False
            winning_turtle=turtle.pencolor()
            if winning_turtle==user_bet:
                print(f"You've won! The winner is {winning_turtle}!")
            else:
                print(f"You've lost! The winner is {winning_turtle}!")
        rand_distance=random.randint(0,10)
        turtle.fd(rand_distance)

screen.exitonclick()