from tkinter import *
from tkinter import filedialog

# Define variables
BGCOLOR = 'gray'
BGCOLOR2 = 'gray77'

# Define Window
root = Tk()
root.geometry("500x500")
root.title('File Counter')
root.configure(bg=BGCOLOR)


# Define functions
def clear_text():
    # Since word_list is an 'entry' field, you must specify the start index
    # location and end location.
    word_list.delete(0, END)

    # Since answer is a text field, you must specify the start line and
    # end location
    answer.delete('1.0', END)


# Opens dialog box to select file
def open_file():
    root.filename = filedialog.askopenfilename()

# Create entry box for word_list
word_list = Entry(root, width=55)
word_list.place(x=0, y=0)

# Create buttons
file = Button(root, text='Select file', width=55, highlightbackground=BGCOLOR,
              command=lambda: open_file())
file.place(x=0, y=30)

count = Button(root, text='Count Words', width=55, highlightbackground=BGCOLOR)
count.place(x=0, y=60)

clear = Button(root, text='Clear Text', width=55, highlightbackground=BGCOLOR,
               command=lambda: clear_text())
clear.place(x=0, y=90)

# Create answer box
answer = Text(root, height=30, width=500, bg=BGCOLOR2)
answer.place(x=0, y=120)

# Refresh 'root' and continue to run
root.mainloop()
