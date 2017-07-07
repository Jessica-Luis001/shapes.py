from turtle import *
import math

# Name your Turtle.
marie = Turtle()
color = input("What color would you like?")
sides = input("How many sides would you like?")
steps = input("How many steps would you like?")

# Set Up your screen and starting position.
marie.penup()
setup(500,300)
x_pos = -250
y_pos = -150
marie.setposition(x_pos, y_pos)

### Write your code below:
answer = input("What color would you like?")
intanswer = int(answer)
answer = input("How many sides would you like?")
intanswer = int(answer)

marie.pendown()
marie.speed(10)
marie.pencolor(color)

def square():
    marie.begin_fill()
    marie.fillcolor(color)
    for square in range(4):
        marie.forward(50)
        marie.right(90)
    marie.end_fill()
    print("This is a square.")
marie.penup()
square()

marie.pendown()
def large_square():
    for large_square in range (4):
        marie.forward(50)
        marie.left(90)
        marie.forward(50)
        print("This is a large_square")
marie.penup()
large_square()

# Close window on click.
exitonclick()
