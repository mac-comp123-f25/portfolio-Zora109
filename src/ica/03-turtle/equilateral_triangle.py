import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.color('dark red'); t.fillcolor('salmon'); t.pensize(3)

t.begin_fill()
for _ in range(3):
    t.forward(220)
    t.left(120)
t.end_fill()

s.exitonclick()
