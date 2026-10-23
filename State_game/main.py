#for indian_states i have created a csv file
# import pandas
#
# data_dict = {
#     "State": [
#         "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
#         "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
#         "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
#         "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
#         "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
#         "Uttar Pradesh", "Uttarakhand", "West Bengal"
#     ],
#     "X": [
#         80.64, 93.62, 91.73, 85.14, 81.63,
#         73.82, 72.63, 76.77, 77.17, 85.34,
#         77.59, 76.95, 77.41, 72.88, 93.94,
#         91.88, 92.72, 94.11, 85.84, 76.77,
#         75.79, 88.61, 80.27, 78.49, 91.28,
#         80.94, 78.03, 88.36
#     ],
#     "Y": [
#         16.51, 27.10, 26.14, 25.61, 21.25,
#         15.49, 23.22, 30.73, 31.10, 23.36,
#         12.97, 8.52, 23.26, 19.07, 24.82,
#         25.57, 23.73, 25.67, 20.27, 30.73,
#         26.91, 27.33, 13.08, 17.38, 23.83,
#         26.85, 30.32, 22.57
#     ]
# }
#
# df=pandas.DataFrame(data_dict)
# df.to_csv("states.csv")

import turtle
import pandas

screen=turtle.Screen()
screen.setup(750,750)
screen.title("Indian States Game")
image="blank_img.gif"
screen.addshape(image) #for adding image to our screen
turtle.shape(image)

#code shows coordinate of place when clicked
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor) 
# turtle.mainloop()

data=pandas.read_csv("states.csv")
all_states=data["State"].to_list()
guessed_states=[]

while len(guessed_states)<28:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                  prompt="What's another state's name?").title()
    if answer_state=="Exit":
        missing_states=[append(state) for state in all_states if state not in guessed_states]
        # new_data=pandas.DataFrame(missing_states) it will create new csv file for missing states
        # new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["State"]==answer_state]
        t.goto(x=state_data["X"].item(),y=state_data["Y"].item())
        t.write(answer_state)

