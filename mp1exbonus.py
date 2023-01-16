from turtle import *

x = 100
forward(x)
left(90)
for i in [0,1,2,3,4,5,6,7,8,9,10]:
    forward(x)
    left(90)
    forward(x)
    left(90)
    x = x - 10

hideturtle()
exitonclick()