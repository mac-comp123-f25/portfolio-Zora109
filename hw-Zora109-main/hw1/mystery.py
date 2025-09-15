usrNum = input("Enter size: ")          # Prompt the user for the square size (string)
num = int(usrNum)                       # Convert input to integer for arithmetic/repetition

print("* " * num)                       # Top border: repeat "* " num times (e.g., "* * * * ")

for i in range(1, num - 1):             # Loop over interior rows (exclude first and last row)
    space = "  " * (num - 2)            # Interior gap: two spaces per missing column to match the "* " spacing
    print("*" + space + " *")           # Left border "*", interior spaces, then " *" for the right border

print("* " * num)                       # Bottom border: same as the top border



