import turtle
s = turtle.Screen()

a = turtle.Turtle(); a.shape('turtle'); a.color('purple')
for _ in range(5): a.forward(150); a.right(144)

b = turtle.Turtle(); b.shape('turtle'); b.color('teal')
b.penup(); b.goto(-180, -40); b.pendown()
for _ in range(5): b.forward(120); b.right(144)

s.exitonclick()

