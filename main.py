from tkinter import *

# Create a tkinter window called root.
root = Tk()

# Provide a title for the window.
root.title("Melody")

# Define the size of the window
root.geometry("300x300")

# Add a text label to the window
text = Label(root, text="Let\'s make some noise!")
text.pack()

# Refreshes 'root' window
root.mainloop()
