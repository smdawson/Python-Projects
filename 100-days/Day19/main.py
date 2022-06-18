from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_counter_clockwise():
    tim.left(10)


# Will also work
# def move_counter_clockwise():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)


def move_clockwise():
    tim.right(10)


def turtle_reset():
    tim.reset()


screen.setup(width=960, height=810, startx=2400)
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(turtle_reset, "c")
screen.exitonclick()
