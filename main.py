import random
import turtle as t
from turtle import Screen
from random import Random
tim =t.Turtle()
t.colormode(255)
# tim.shape('turtle')
# tim.color('coral')
# tim.forward(100)
# tim.right(90)#Have the turtle turn south from facing east

# def draw_square():
#     for _ in range(3):
#         tim.forward(100)
#         tim.right(90)
#
# draw_square()

# def draw_dashline():
#     for _ in range(15):
#         tim.forward(10)
#         tim.pendown()
#         tim.forward(10)
#         tim.penup()
# draw_dashline()

# colors =['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
#          'cyan', 'turquoise', 'lightgreen', 'cyan', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']
#

# def draw_diff_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for side in range(3,11):
#     tim.pencolor(random.choice(colors))
#     draw_diff_shape(side)

#
# def random_walk(n):
#     tim.pencolor(random.choice(colors))
#     tim.pensize(10)
#     direction = random.choice(['n','s','e','w'])
#     if direction == 'n':
#         tim.left(50)
#     elif direction == 's':
#         tim.right(50)
#     elif direction == 'e':
#         tim.forward(50)
#     else:
#         tim.back(50)
#
# for n in range(200):
#     random_walk(n)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# def random_walk():
#     directions = [0, 90, 180, 270]
#     tim.pensize(10)
#     tim.speed(0)
#     for _ in range(200):
#         tim.color(random_color())
#         tim.forward(30)
#         tim.setheading(random.choice(directions))
#
#
# random_walk()
# def draw_spiral():
#     tim.pensize(1)
#     tim.speed(0)
#     for i in range(1, 37):
#         tim.pencolor(random_color())
#         tim.circle(100)
#         tim.right(10)

#draw_spiral()
tim.speed(0)
def draw_spirograph(sz_of_gap):
    for _ in range(int(360/sz_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + sz_of_gap)

draw_spirograph(5)
screen = Screen()
screen.exitonclick()