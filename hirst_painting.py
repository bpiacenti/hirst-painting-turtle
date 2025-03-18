# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst_image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Code above used to get initial RGB values via extraction from a jpeg, can use a different
# image if you want different colors

import random
import turtle as tmod
t = tmod.Turtle()
tmod.colormode(255)
hirst_colors = [(232, 206, 81), (227, 146, 86), (216, 227, 219), (231, 223, 226), (216, 224, 229), (157, 15, 23), (117, 167, 188), (30, 110, 158), (234, 83, 44), (124, 175, 145), (7, 98, 38), (172, 20, 15), (30, 130, 48), (182, 185, 27), (200, 63, 27), (11, 42, 76), (16, 62, 41), (238, 202, 8), (136, 83, 96), (91, 15, 25), (49, 166, 77), (37, 27, 23), (176, 135, 148), (6, 66, 137), (50, 151, 196), (215, 67, 72), (232, 169, 161), (167, 208, 174), (78, 133, 185)]

t.hideturtle()
t.speed("fastest")
t.pu()
t.setheading(225)
t.forward(300)
t.setheading(0)
num_dots = 100

for dots in range(1, num_dots + 1):
    t.dot(20, random.choice(hirst_colors))
    t.forward(50)

    if dots % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = tmod.Screen()
screen.exitonclick()