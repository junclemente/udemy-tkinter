from tkinter import *

# Create tkinter window called root
root = Tk()

# Define title of window
root.title("Window Title")

# Define size of window
root.geometry("300x300")

# Prevent window from being resized
root.resizable(width=False, height=False)

# StringVar is used to declare a Tkinter string variable
name = StringVar()


def print_name():
    name.set('Code and Light')


def print_hello_world():
    name.set('Hello, World!')


def print_movie():
    name.set('Hamilton: The Movie!')


# Define button
btn1 = Button(root, text='click me!', command=lambda: print_name())
btn1.place(x=0, y=0)

btn2 = Button(root, text='Hello!', command=lambda: print_hello_world())
btn2.place(x=100, y=0)

btn3 = Button(root, text='Movie!', command=lambda: print_movie())
btn3.place(x=200, y=0)

# Define label with a textvariable assigned to name
label = Label(root, textvariable=name)
label.place(x=100, y=150)


# Refreshes 'root' window and continues to run it
root.mainloop()
