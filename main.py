from tkinter import *
from pygame import mixer


# Create a tkinter window called root.
root = Tk()

# Initialize pygame mixer
mixer.init()

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
def play_music():
    mixer.music.load("BrokeForFree-NightOwl.mp3")
    mixer.music.play()


# Add an image to use as a button
play_photo = PhotoImage(file="play-button64.gif")
play_button = Button(root, image=play_photo, command=play_music)
play_button.pack()

# Refreshes 'root' window
root.mainloop()
