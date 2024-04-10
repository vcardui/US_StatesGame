import turtle
import pandas

ALIGNMENT = 'center'
FONT = ("Arial", 14, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

data_states = pandas.read_csv("50_states.csv")
data_states_list = data_states.state.to_list()

def winprompt():
    pen.color('DeepSkyBlue4')
    pen.fillcolor('LightSkyBlue1')
    pen.pensize(width=3)
    pen.begin_fill()
    pen.goto(-140,80)
    pen.pendown()
    pen.forward(270)
    pen.seth(270)
    pen.forward(125)
    pen.seth(180)
    pen.forward(270)
    pen.seth(90)
    pen.forward(125)
    pen.end_fill()
    pen.penup()
    pen.goto(0,0)
    pen.write(f"Game Over\nSee you soon :)", align=ALIGNMENT, font=("Courier", 20, "bold"))

emptyList = []
while data_states_list != emptyList:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        break
    if answer_state in data_states_list:
        data_states_list.remove(answer_state)
        xcor = data_states[data_states.state == answer_state].x
        ycor = data_states[data_states.state == answer_state].y
        pen.goto(int(xcor), int(ycor))
        pen.write(f"{answer_state}", align=ALIGNMENT, font=FONT)

    print(data_states_list)

if data_states_list == emptyList:
    winprompt()
