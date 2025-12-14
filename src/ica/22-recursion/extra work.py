import turtle
import math


def calc_next_size(size):
    """Helper function to compute next segment size (provided in assignment)."""
    return size / math.sqrt(2)


def draw_levy(turt, size, reps):
    """
    Draw the Levy C Curve recursively.

    Base case:
        - If reps == 1, draw a straight line of length size.
    Recursive case (reps > 1):
        1. Compute smaller size using calc_next_size()
        2. Turn turtle left 45°
        3. Recursively draw first half
        4. Turn turtle right 90°
        5. Recursively draw second half
        6. Turn turtle left 45° to restore direction
    """
    if reps == 1:
        turt.forward(size)
    else:
        new_size = calc_next_size(size)
        turt.left(45)
        draw_levy(turt, new_size, reps - 1)
        turt.right(90)
        draw_levy(turt, new_size, reps - 1)
        turt.left(45)


def check_draw_levy(size, reps):
    """Helper function to quickly test Levy C Curve."""
    scr = turtle.Screen()
    scr.title(f"Levy C Curve (size={size}, reps={reps})")
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")

    draw_levy(t, size, reps)

    scr.exitonclick()


if __name__ == "__main__":
    # Try different reps values (1–10) for increasing detail
    check_draw_levy(300, 1)
    check_draw_levy(300, 4)
    check_draw_levy(300, 8)
