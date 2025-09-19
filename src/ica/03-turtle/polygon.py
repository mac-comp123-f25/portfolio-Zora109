import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.color('navy'); t.fillcolor('skyblue')

n = 6
L = 120

t.begin_fill()
for _ in range(n):
    t.forward(L); t.left(360/n)
t.end_fill()

s.exitonclick()
