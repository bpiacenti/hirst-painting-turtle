# import random
# import turtle
#
# t = turtle.Turtle()
# screen = turtle.Screen()
# screen.screensize(1500, 1500)
#
#
# colors = ["red", "blue", "green", "orange", "yellow", "indigo", "violet"]
# directions = [0, 90, 180, 270]
#
# turtle.colormode(255)
#
# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g ,b)
#     return color
#
# t.shape("turtle")
# # t.pensize(15)
# t.speed("fastest")
#
# # t.color(rand_color())
# #
# # t.circle(100)
#
# def draw_spiro(size_of_gap):
#     for i in range(int(360 / size_of_gap)):
#         t.color(rand_color())
#         t.circle(100)
#         t.setheading(t.heading() + size_of_gap)
#
# draw_spiro(5)
#
#
#
# turtle.exitonclick()

