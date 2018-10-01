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


# Define button
btn = Button(root, text='click me!', command=lambda: print_name())
btn.place(x=0, y=0)

# Define label with a textvariable assigned to name
label = Label(root, textvariable=name)
label.place(x=100, y=150)


# Refreshes 'root' window and continues to run it
root.mainloop()
