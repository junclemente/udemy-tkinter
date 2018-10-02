from tkinter import *
from tkinter import filedialog

# Define variables
BGCOLOR = 'gray'
BGCOLOR2 = 'gray77'
count_result = dict()

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


# Opens text file and converts each line into a list
def count_text(file):
    file_open = open(str(file), 'r')
    full_text = file_open.readlines()
    file_open.close()

    # Iterates through all words entered in 'word_list'
    for word in word_list.get().split(', '):
        # Compares each item in full_text to word and
        # adds count to count_result
        for text in full_text:
            if word in count_result:
                count_result[word] = count_result[word] + text.count(word)
            else:
                count_result[word] = text.count(word)

    # Clears answer textbox
    answer.delete('1.0', END)

    # Iterates through count_result dict and assigns result to answer textbox
    for k, v in count_result.items():
        answer.insert('1.0', '{0} {1} \n'.format(k, v))

    # Clears the count_result dict
    count_result.clear()


# Create entry box for word_list
word_list = Entry(root, width=55)
word_list.place(x=0, y=0)

# Create buttons
file = Button(root, text='Select file', width=55, highlightbackground=BGCOLOR,
              command=lambda: open_file())
file.place(x=0, y=30)

count = Button(root, text='Count Words', width=55, highlightbackground=BGCOLOR,
               command=lambda: count_text(root.filename))
count.place(x=0, y=60)

clear = Button(root, text='Clear Text', width=55, highlightbackground=BGCOLOR,
               command=lambda: clear_text())
clear.place(x=0, y=90)

# Create answer box
answer = Text(root, height=30, width=500, bg=BGCOLOR2)
answer.place(x=0, y=120)

# Refresh 'root' and continue to run
root.mainloop()
