import tkinter as tk
import turtle
import random


def check_draw_tree(sz):
    """Tester function for the draw_tree"""
    # setup window
    win = tk.Toplevel()
    win.title(f"Tree Fractal {sz}")
    win_size = sz * 7
    cv = tk.Canvas(win, width=win_size, height=win_size)
    cv.pack()
    ts = turtle.TurtleScreen(cv)
    t = turtle.RawTurtle(ts)

    # set up turtle
    t.left(90)
    t.up()
    t.backward(sz * 3)
    t.down()
    t.speed(0)
    t.color("green")

    # draw the tree
    draw_tree(sz, t)


def draw_tree(branch_len, turt):
    """
    Modified fractal tree with slight randomness and drooping branches.
    Differences from original:
      - Random angle variation for more natural look.
      - Unequal branch lengths for asymmetry.
      - Slightly reduced right branch angle for a "weeping" tree shape.
    """
    if branch_len > 5:
        angle = random.randint(15, 25)         # small random turn angle
        shrink = random.randint(10, 18)        # vary branch shortening

        turt.forward(branch_len)
        turt.right(angle)
        draw_tree(branch_len - shrink, turt)   # right branch shorter

        turt.left(angle * 2)                   # left branch turns wider
        draw_tree(branch_len - shrink - 5, turt)

        turt.right(angle)                      # reset heading
        turt.backward(branch_len)


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    # test multiple sizes
    check_draw_tree(30)
    check_draw_tree(75)
    check_draw_tree(125)

    root.mainloop()
