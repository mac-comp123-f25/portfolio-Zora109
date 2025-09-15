import turtle
s = turtle.Screen()
s.bgcolor('wheat')
def zigzag(t, steps=40, step=8, angle=30):
    for i in range(steps):
        t.forward(step)
        t.left(angle if i % 2 == 0 else -angle)

# three turtles, three colors
t1 = turtle.Turtle(); t1.color('red');   t1.pensize(3); t1.speed(0)
t2 = turtle.Turtle(); t2.color('magenta'); t2.pensize(3); t2.speed(0)
t3 = turtle.Turtle(); t3.color('navy');  t3.pensize(3); t3.speed(0)

# positions & headings
t1.penup(); t1.goto(-320, 120); t1.setheading(20);  t1.pendown()
t2.penup(); t2.goto(-320, 70);  t2.setheading(0);   t2.pendown()
t3.penup(); t3.goto(-320, 20);  t3.setheading(-20); t3.pendown()

for t in (t1, t2, t3):
    zigzag(t)

s.exitonclick()


