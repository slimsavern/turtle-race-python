import random
from turtle import Turtle, Screen


screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start_position = -150
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make a bet","Which turtle will win the race?")

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230,y=start_position)
    start_position += 50
    turtles.append(new_turtle)

end_game = False

while not end_game:
    for turtle in turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            end_game = True
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else:
                print(f"You lost {winning_color} won the race")

screen = Screen()
screen.exitonclick()
