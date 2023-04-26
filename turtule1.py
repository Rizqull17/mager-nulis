'''
import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.width(2)
t.speed(15)

col=('yellow','green','red','blue')

for i in range(300):
    t.pencolor(col[i%4])
    t.forward(i*4)
    t.right(137)
'''

from turtle import*
speed(2)
bgcolor("white")
penup()
goto(-50, 60)
pendown()
color("#00adef")
begin_fill()
goto(100, 100)
goto(100, -100)
goto(-50, -60)
goto(-50, 60)

end_fill()
color("white")

goto(15, 100)
color("white")
width(10)
goto(15, -100)
penup()
goto(100, 0)
pendown()
goto(-100, 0)

done()
