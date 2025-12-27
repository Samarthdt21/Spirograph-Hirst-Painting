# Colorgram package is needed to extract colors from a image.
# import colorgram as c
# colors=c.extract("image.jpg",10)
# rgb_colours=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colours.append((r,g,b))
#
# print(rgb_colours)
from turtle import *
import random
tim=Turtle()
tim.hideturtle()
colormode(255)
tim.speed("fastest")
tim.penup()
color_list=[(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1,101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen=Screen()
screen.exitonclick()