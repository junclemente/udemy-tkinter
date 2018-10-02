from tkinter import *


# Define static variables
COLOR = 'gray55'

# Define root window
root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)
root.title("Email Sender")
root.configure(bg=COLOR)


# Define Frames
top = Frame(root, width=800, height=50, bg="black")
top.pack(side=TOP)

bottom = Frame(root, width=800, height=50, bg="black")
bottom.pack(side=BOTTOM)

left = Frame(root, width=600, height=400, bg="red")
left.pack(side=LEFT)

right = Frame(root, width=200, height=400, bg="blue")
right.pack(side=RIGHT)

# Execute  root window
root.mainloop()