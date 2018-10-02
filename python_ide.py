from tkinter import *

# Declare variables
BGCOLOR = "gray"

# Define window
root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)
root.title("Run Python Code")
root.configure(bg=BGCOLOR)

# Define frames
top = Frame(root, width=800, height=50, bg="black")
top.pack(side=TOP)

bottom = Frame(root, width=800, height=450, bg="red")
bottom.pack(side=BOTTOM)


root.mainloop()