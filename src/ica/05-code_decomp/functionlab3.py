import turtle
import math

def drawFiveCircles(turt, radius, centerX, centerY):

    turt.penup()
    turt.goto(centerX, centerY)
    turt.pendown()
    for _ in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

"""
Program purpose:
Draw five flowers. For each flower, five larger green circles (sepals) and
five smaller red/coral circles (petals) are arranged by turning 72° between
circles around a central point. A purple filled disk is drawn near the center,
and a gold turtle-shaped stamp (bee) is placed near the center. The script
uses four turtles: sepalTurtle, petalTurtle, centerTurtle, stampTurtle.
This file corresponds to STEP 3: sepals and petals have been refactored
into a drawFiveCircles() function; the center disk and bee remain inline.
"""

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

# ---------------- Flower 1 at (0, 0) ----------------
drawFiveCircles(sepalTurtle, 50, 0, 0)
drawFiveCircles(petalTurtle, 25, 0, 0)

centerTurtle.up()
centerTurtle.goto(0, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2, 0)
stampTurtle.down()
stampTurtle.stamp()

# ---------------- Flower 2 at (0, 220) ----------------
drawFiveCircles(sepalTurtle, 50, 0, 220)
drawFiveCircles(petalTurtle, 25, 0, 220)

centerTurtle.up()
centerTurtle.goto(0, 205)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2, 220)
stampTurtle.down()
stampTurtle.stamp()

# ---------------- Flower 3 at (220, 0) ----------------
drawFiveCircles(sepalTurtle, 50, 220, 0)
drawFiveCircles(petalTurtle, 25, 220, 0)

centerTurtle.up()
centerTurtle.goto(220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(218, 0)
stampTurtle.down()
stampTurtle.stamp()

# ---------------- Flower 4 at (0, -220) ----------------
drawFiveCircles(sepalTurtle, 50, 0, -220)
drawFiveCircles(petalTurtle, 25, 0, -220)

centerTurtle.up()
centerTurtle.goto(0, -235)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2, -220)
stampTurtle.down()
stampTurtle.stamp()

# ---------------- Flower 5 at (-220, 0) ----------------
drawFiveCircles(sepalTurtle, 50, -220, 0)
drawFiveCircles(petalTurtle, 25, -220, 0)

centerTurtle.up()
centerTurtle.goto(-220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-222, 0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()
