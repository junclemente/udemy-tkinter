from tkinter import *

# Create tkinter window called root
root = Tk()

# Define title of window
root.title("Window Title")

# Define size of window
root.geometry("300x300")

# Prevent window from being resized
root.resizable(width=False, height=False)


word = StringVar()

entry = Entry(root)
entry.place(x=50, y=0)


def get_name():
    print(entry.get())
    word.set(entry.get())
    entry.insert(0, 'This is my name: ')

label = Label(root, text='Name: ')
label.place(x=0, y=0)

btn = Button(root, text='get name', command=lambda: get_name())
btn.place(x=100, y=100)

display = Label(root, textvariable=word)
display.place(x=100, y=150)



# Refreshes 'root' window and continues to run it
root.mainloop()
