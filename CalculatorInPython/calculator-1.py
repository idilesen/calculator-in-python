from tkinter import Tk, Entry, Button

# This line is for GUI


def write(x: int) -> None:
    """
    This function writes the input number to the display.

    Args:
        x: The number to be written.
    """
    s = len(start.get())
    start.insert(s, str(x))


# This function is for taking an input and writing that input on screen


calculation: int = 7
s1: float = 0
# The calculation variable keeps the data of operation
# First it assigned to 7, but later the value will be changed
# s1 variable is keeping the first number


def operations(x: int) -> None:
    """
    This function determines the chosen operation and stores values.

    Args:
        x: The operation code (0: +, 1: -, 2: *, 3: /).
    """
    global calculation
    calculation = x
    global s1
    s1 = float(start.get())
    print(calculation)
    print(s1)
    start.delete(0, "end")


# This function determines the operation
# x is the operation that the user chooses
# the value assigned to the calculation variable determines which operation to take
# The first number entered by the user is assigned to the s1 variable
# and the input part is deleted with the start.delete() method

s2: float = 0
# s2 variable is keeping the second number


def calculate() -> None:
    """
    This function performs the calculation and displays the result.
    """
    global s2
    s2 = float(start.get())
    print(s2)
    global calculation
    result = 0
    if calculation == 0:
        result = s1 + s2
    elif calculation == 1:
        result = s1 - s2
    elif calculation == 2:
        result = s1 * s2
    elif calculation == 3:
        result = s1 / s2
    start.delete(0, "end")  # Deleting the first number from the screen before entering the second number
    start.insert(0, str(result))


# This functions for the calculation
# First, it assigns the second number to variable s2
# Then, it performs the correct operation according
# to the calculation variable and prints the result to the screen

window = Tk()
window.title("CALCULATOR")
window.geometry("500x500")
window.configure(bg="lightpink")
# Tk object is created from the tkinter library
# The window title is set to "CALCULATOR"
# The size of the window is set to 500x500 pixels
# The background color is lightpink

start: Entry = Entry(font="Verdana 14 bold", width=20, justify=RIGHT)
start.place(x=80, y=20)
# This part is for taking entry
# Entry part font is vernada 14 bold
# Width is 20 characters and it is aligned to the right

b: list[Button] = []
for i in range(1, 10):
    b.append(
        Button(
            text=str(i),
            font="Verdana 14 bold",
            width=4,
            command=lambda x=i: write(x),
            bg="lightpink",
        )
    )
# Creates buttons that display numbers 1 through 9 and adds them to a list
# write() function is assigned to each button.

counter = 0
for i in range(0, 3):
    for j in range(0, 3):
        b[counter].place(x=80 + j * 70, y=80 + i * 70)
        counter += 1
# This part is located the number boxes in order

operation: list[Button] = []
for i in range(0, 4):
    operation.append(
        Button(
            fg="black",
            bg="blue",
            font="Verdana 14 bold",
            width=4,
            command=lambda x=i: operations(x),
        )
    )
operation[0]["text"] = "+"
operation[1]["text"] = "-"
operation[2]["text"] = "*"
operation[3]["text"] = "/"
# It creates 4 operation boxes and adding them in a list
