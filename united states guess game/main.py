import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()

CORRECT_ANSWER_COUNT = 0


while game_is_on:

    answer_state = screen.textinput(title=f"{CORRECT_ANSWER_COUNT}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    for _ in state_list:
        if _ == answer_state:
            CORRECT_ANSWER_COUNT += 1
            index = state_list.index(answer_state)
            tim = turtle.Turtle()
            tim.hideturtle()
            tim.penup()
            tim.goto(x_list[index], y_list[index])
            tim.write(arg=answer_state)
            
    if CORRECT_ANSWER_COUNT == 50:
        game_is_on = False





    print(answer_state)



turtle.mainloop()