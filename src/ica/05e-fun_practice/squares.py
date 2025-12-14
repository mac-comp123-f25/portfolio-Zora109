# squares.py
import turtle

def draw_nested_squares(tt):
    """
    Draw nested squares with side lengths 10, 20, ..., 80.
    The turtle 'tt' is used to draw; each square is centered.
    """
    tt.speed(0)
    tt.hideturtle()

    for side in range(10, 90, 10):  # 10,20,...,80
        # Move to lower-left corner so the square is centered at (0,0)
        tt.penup()
        tt.goto(-side / 2, -side / 2)
        tt.pendown()

        # Draw one square
        for _ in range(4):
            tt.forward(side)
            tt.left(90)

if __name__ == "__main__":
    win = turtle.Screen()
    tt = turtle.Turtle()
    draw_nested_squares(tt)
    win.exitonclick()
