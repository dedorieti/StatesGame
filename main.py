import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
# screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("Black")
# screen.tracer(0)
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
game_is_on = True
score = 0

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
all_states = list(map(str.lower, all_states))

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state name")
    if answer_state == 'exit':
        game_is_on = False
    if answer_state.lower() in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state.str.lower() == answer_state.lower()]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        score += 1
        all_states.remove(answer_state.lower())

states_to_learn = pd.DataFrame(all_states)
states_to_learn.columns = ['states_to_learn']
states_to_learn.to_csv("states_to_learn.csv")
screen.exitonclick()
