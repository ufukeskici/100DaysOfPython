import turtle
import random

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243),
              (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),  (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()

def draw_one_line():
    x = -250
    y = -250
    for line in range(10):
        tim.hideturtle()
        tim.speed('fastest')
        tim.penup()
        tim.setpos(x, y)
        for dots in range(10):
            tim.pendown()
            # dot_color = random.choice(color_list)
            # tim.color(dot_color)
            tim.dot(20, random.choice(color_list))
            tim.penup()
            if dots != 9:
                tim.fd(50)
        y += 50

draw_one_line()
screen.exitonclick()