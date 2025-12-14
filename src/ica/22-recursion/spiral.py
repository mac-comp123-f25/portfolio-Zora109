import turtle


def spiral_in(spiro_turt, side_len):
    """
    Draw a rectangular spiral from outside to inside by recursion.
    Each recursive step draws one side, turns 90°, then recurses with side_len - 5.
    Stops when side_len <= 5.
    """
    if side_len <= 5:
        return
    spiro_turt.forward(side_len)
    spiro_turt.right(90)
    spiral_in(spiro_turt, side_len - 5)


def check_spiral_in(size: int) -> None:
    """A faster way to test spiral_in function"""
    scr = turtle.Screen()
    turt = turtle.Turtle()
    turt.speed(0)  # optional: fastest drawing
    spiral_in(turt, size)
    scr.exitonclick()


if __name__ == '__main__':
    check_spiral_in(200)  # try 200 for a full spiral; adjust as needed
