import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Happy Fr5iendship Day 💛")


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)



def draw_heart(x, y, color):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()
    pen.setheading(0)


def write_message(msg, color, y_pos):
    pen.up()
    pen.goto(0, y_pos)
    pen.color(color)
    pen.write(msg, align="center", font=("Comic Sans MS", 28, "bold"))

colors = ["red", "hotpink", "yellow", "orange","purple","green"]


for i in range(6):
    pen.clear()
    draw_heart(0, -100, random.choice(colors))
    write_message("Happy Friendship Day!", random.choice(colors), 100)
    time.sleep(0.7)


pen.clear()
write_message("You're the Best 💛", "deeppink", 0)

input("Press Enter to exit...")
turtle.done()

