import turtle
import math

def drawFiveCircles(turt, radius, centerX, centerY):
    """
    Draw 5 filled circles of the same radius around a center point by
    turning 72 degrees between circles (replicates the starter code behavior).
    Inputs:
      turt     : the turtle used for drawing (already configured with colors)
      radius   : circle radius (e.g., 50 for sepals, 25 for petals)
      centerX  : x coordinate of the flower center (where the turtle stands)
      centerY  : y coordinate of the flower center
    Effect:
      Moves to (centerX, centerY), then draws 5 circles with begin_fill/end_fill,
      turning left(72) after each circle. This matches the original hard-coded steps.
    """
    turt.penup()
    turt.goto(centerX, centerY)
    turt.pendown()
    for _ in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

def drawCenterCircle(turt, flowerCenterX, flowerCenterY):
    """
    Draw the filled center disk of a flower, given the flower's overall center.
    Inputs:
      turt           : turtle configured for the center disk color
      flowerCenterX  : overall flower center x
      flowerCenterY  : overall flower center y
    Effect:
      Draws a filled circle of radius 15, centered slightly below the exact
      flower center (the classic turtle trick: goto(x, y - r) then circle(r)).
    """
    r = 15
    turt.penup()
    turt.goto(flowerCenterX, flowerCenterY - r)
    turt.setheading(0)
    turt.pendown()
    turt.begin_fill()
    turt.circle(r)
    turt.end_fill()

def drawBee(turt, flowerCenterX, flowerCenterY):
    """
    Stamp a 'bee' (a turtle-shaped stamp) near the flower center.
    Inputs:
      turt           : turtle configured with shape('turtle') and bee color
      flowerCenterX  : overall flower center x
      flowerCenterY  : overall flower center y
    Effect:
      Stamps the turtle at a slight left offset (-2, 0) from the center,
      matching the starter code's placement.
    """
    turt.penup()
    turt.goto(flowerCenterX - 2, flowerCenterY)
    turt.setheading(0)
    turt.pendown()
    turt.stamp()

"""
Program purpose (STEP 5):
Draw five flowers. Sepals and petals are drawn via drawFiveCircles().
The center disk is drawn via drawCenterCircle(). The 'bee' is now
abstracted into drawBee().
Turtles:
  - sepalTurtle  : dark green / spring green
  - petalTurtle  : dark red / light coral
  - centerTurtle : purple4
  - stampTurtle  : gold, shape 'turtle'
"""

# --- Window / turtles setup ---
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

# ------------ Flower centers ------------
centers = [
    (0, 0),
    (0, 220),
    (220, 0),
    (0, -220),
    (-220, 0),
]

# ------------ Draw all five flowers ------------
for (cx, cy) in centers:
    # sepals & petals via Step 3 function
    drawFiveCircles(sepalTurtle, 50, cx, cy)
    drawFiveCircles(petalTurtle, 25, cx, cy)

    # center disk via Step 4 function
    drawCenterCircle(centerTurtle, cx, cy)

    # NEW in Step 5: bee via function
    drawBee(stampTurtle, cx, cy)

win.exitonclick()
