"""
This script draws a robot using turtles
"""
import turtle

# Variable Declaration
side = 200
circ = int(side/6)

# Setup turtle & screen
scr = turtle.Screen()
trt = turtle.Turtle()  # BUGFIX: misspelled class name 'Trtle' -> 'Turtle'
trt.speed(0)
trt.ht()

scr.bgcolor("pale green")
trt.color("gray")
trt.width(3)

# Move turtle

# Body / Head
trt.up()  # BUGFIX: method call missing parentheses
trt.goto((-1/2) * side, (-1/2) * side)
trt.down()

for i in range(4):
    trt.forward(side)
    trt.left(90)

# Left Eye
trt.up()
trt.goto((-1/4)*side, (1/4)*side)
trt.down()

trt.dot(circ)

# Right Eye
trt.up()
trt.goto((1/4)*side, (1/4)*side)
trt.down()

trt.dot(circ)

# Mouth
trt.up()
trt.goto((-3/16)*side, (-1/4)*side)
trt.down()

for i in range(2):
    trt.forward((3/8)*side)
    trt.left(90)
    trt.forward(side/8)
    trt.left(90)

# left ear
trt.up()
trt.goto((-3/8)*side, (1/2)*side)
trt.down()

for i in range(3):
    trt.forward((1/4)*side)
    trt.left(120)  # BUGFIX: wrong turn angle (30) -> 120 for triangle

# right ear
trt.up()
trt.goto((1/8)*side, (1/2)*side)
trt.down()

for i in range(3):
    trt.forward((1/4)*side)
    trt.left(120)

# left leg
trt.up()
trt.goto((-3/8)*side, (-7/8)*side)  # BUGFIX: extra ')' at end
trt.down()

for i in range(2):
    trt.forward((1/4)*side)
    trt.left(90)
    trt.forward((3/8)*side)
    trt.left(90)

trt.up()
trt.goto((-1/2)*side, -side)  # BUGFIX: missing '*' between (-1/2) and side
trt.down()

for i in range(2):
    trt.forward((3/8)*side)
    trt.left(90)
    trt.forward((1/8)*side)
    trt.left(90)

# right leg
trt.up()
trt.goto((1/8)*side, (-7/8)*side)
trt.down()

for i in range(2):
    trt.forward((1/4)*side)
    trt.left(90)
    trt.forward((3/8)*side)
    trt.left(90)

trt.up()
trt.goto((1/8)*side, -side)
trt.down()

for i in range(2):
    trt.forward((3/8)*side)
    trt.left(90)
    trt.forward((1/8)*side)
    trt.left(90)

# left arm
trt.up()
trt.goto((-3/4)*side, 0)
trt.down()

for i in range(2):
    trt.forward((1/4)*side)
    trt.left(90)
    trt.forward((1/8)*side)
    trt.left(90)

# right arm
trt.up()
trt.goto((1/2)*side, 0)
trt.down()

for i in range(2):
    trt.forward((1/4)*side)
    trt.left(90)
    trt.forward((1/8)*side)
    trt.left(90)

scr.exitonclick()
