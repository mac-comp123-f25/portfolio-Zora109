import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.speed(0); t.pensize(2); t.color('medium violet red')

petals = 36
r = 100

for _ in range(petals):
    t.circle(r)
    t.left(360/petals)

t.penup(); t.home(); t.pendown()
t.dot(12)   
s.exitonclick()
