from turtle import *
import random


tim=Turtle()

#Program3 : Spirograph

colormode(255)
tim.pensize(4)
tim.speed("fastest")

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

def draw_spirograph(gap_angle):
    for x in range(int(360/gap_angle)):
       tim.color(random_colour())
       tim.circle(100)
       tim.right(gap_angle)

draw_spirograph(4)




screen = Screen()
screen.exitonclick()














# Program 1
#
# colours=input("colors").split()
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(360 / num_sides)
#
# for x in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(x)



#Program 2: Random Walk
#
# colormode(255)
# def random_colour():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     return (r,g,b)
#
#
# direction=[0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")
#
# for _ in range(100):
#     tim.color(random_colour())
#     tim.forward(40)
#     tim.setheading(random.choice(direction))


#Program3 : Spirograph
#
# colormode(255)
# tim.pensize(1)
# tim.speed("fastest")
#
# def random_colour():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     return (r,g,b)
#
# def draw_spirograph(gap_angle):
#     for x in range(int(360/gap_angle)):
#        tim.color(random_colour())
#        tim.circle(100)
#        tim.right(gap_angle)
#
# draw_spirograph(4)

