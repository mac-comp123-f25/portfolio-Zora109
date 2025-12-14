import turtle


def do_move(turtle_obj, move):
    """
    Checks a move command and directs the turtle_obj accordingly.

    Args:
      turtle_obj: The turtle object to command.
      move: A string representing the desired move ('f', 'b', 'l', or 'r').
    """
    if move == 'f':
        turtle_obj.forward(50)
    elif move == 'b':
        turtle_obj.backward(50)
    elif move == 'l':
        turtle_obj.left(90)
    elif move == 'r':
        turtle_obj.right(90)
    else:
        print("Invalid command! Please use 'f', 'b', 'l', or 'r'.")


# Main part of the script that runs the program
if __name__ == "__main__":
    # Set up the screen and turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.shape('turtle')  # Makes the cursor look like a turtle
    t.speed(5)

    # Main loop to get user commands
    while True:
        user_move = input("Enter your next move (f, b, l, r) or q to quit: ")
        if user_move == 'q':
            break  # Exit the loop if the user types 'q'

        do_move(t, user_move)

    print("Thanks for playing!")
    screen.bye()  # Close the turtle graphics window