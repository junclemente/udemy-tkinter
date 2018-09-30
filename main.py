from tkinter import *
from pygame import mixer

INITIAL_VOLUME = 70


# Create a tkinter window called root.
root = Tk()

# Create menubar
menubar = Menu(root)
root.config(menubar)

# Create sub_menu
sub_menu = Menu(menubar)
menubar.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New Project")
sub_menu.add_command(label="New")

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


# Function to be called when play_button is clicked
def play_music():
    mixer.music.load("BrokeForFree-NightOwl.mp3")
    mixer.music.play()


# Function to stop music when clicked
def stop_music():
    mixer.music.stop()


# Function to adjust volume
def set_music_volume(val):
    # Note: set_volume function takes value from 0 - 1.
    volume = int(val)/100
    mixer.music.set_volume(volume)


# Add an play button image
play_photo = PhotoImage(file="play-button64.gif")
play_button = Button(root, image=play_photo, command=play_music)
play_button.pack()

# Add stop button image
stop_photo = PhotoImage(file="stop64.gif")
stop_button = Button(root, image=stop_photo, command=stop_music)
stop_button.pack()

# Create scale widget to control volume
volume_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL,
                     command=set_music_volume)
volume_scale.set(INITIAL_VOLUME)
mixer.music.set_volume(INITIAL_VOLUME)
volume_scale.pack()


# Refreshes 'root' window
root.mainloop()
