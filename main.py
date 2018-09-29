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


# Function to be called when btn is clicked
def play_button():
    print("Hey! The play button has been pressed.")


# Add an image to use as a button
photo = PhotoImage(file="play-button64.gif")
btn = Button(root, image=photo, command=play_button)
btn.pack()

# Refreshes 'root' window
root.mainloop()
