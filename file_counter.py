from tkinter import *

# Define variables
BGCOLOR = 'gray'
BGCOLOR2 = 'gray77'

# Define Window
root = Tk()
root.geometry("500x500")
root.title('File Counter')
root.configure(bg=BGCOLOR)

# Create entry box for word_list
word_list = Entry(root, width=55)
word_list.place(x=0, y=0)

# Create buttons
file = Button(root, text='Select file', width=55, highlightbackground=BGCOLOR)
file.place(x=0, y=30)

count = Button(root, text='Count Words', width=55, highlightbackground=BGCOLOR)
count.place(x=0, y=60)

clear = Button(root, text='Clear Text', width=55, highlightbackground=BGCOLOR)
clear.place(x=0, y=90)

# Create answer box
answer = Text(root, height=30, width=500, bg=BGCOLOR2)
answer.place(x=0, y=120)

# Refresh 'root' and continue to run
root.mainloop()
