import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
NUMsides=7
len=75
angle=360.0/NUMsides

for i in range(NUMsides) :
    polygon.forward(len) 
    polygon.right(angle)

turtle.done()