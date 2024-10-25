from turtle import *


#we want to paint a house

#step 1: draw a square
width(5)

begin_fill()
color("blue")
forward (200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
end_fill()

# end off square

#drawing door

forward(70)
begin_fill()
color("red")
left(90)
forward(80)  #height off door
right(90)
forward(50)
right(90)
forward(80)
end_fill()

penup()
goto(200, 200)
pendown()

color("GREEN")

begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(25, 125)
pendown()
color("black")

begin_fill()
right(150)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(125, 125)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()




exitonclick()





