from tkinter import *

# Create a tkinter window called root.
root = Tk()

# Define the size of the window
root.geometry("300x300")

# Provide a title for the window.
root.title("Melody")

# Add Icon to window bar
root.iconbitmap(r'melody.ico')

# Add a text label to the window
text = Label(root, text="Let\'s make some noise!")
text.pack()

# Refreshes 'root' window
root.mainloop()
