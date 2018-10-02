from tkinter import *


# Define static variables
COLOR = 'gray55'
CURSOR_WIDTH = 3
BORDER_DEPTH = 4

# Define root window
root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)
root.title("Email Sender")
root.configure(bg=COLOR)


# Define Frames
top = Frame(root, width=800, height=50, bg=COLOR)
top.pack(side=TOP)

bottom = Frame(root, width=800, height=50, bg="red")
bottom.pack(side=BOTTOM)

left = Frame(root, width=600, height=400, bg="blue")
left.pack(side=LEFT)

right = Frame(root, width=200, height=400, bg=COLOR)
right.pack(side=RIGHT)


# Define buttons in 'right' frame
clear_to_btn = Button(right, text="Clear To", font=("arial", 20, "bold"),
                      highlightbackground=COLOR)
clear_to_btn.pack(side=TOP, padx=5, pady=5)

clear_from_btn = Button(right, text="Clear From", font=("arial", 20, "bold"),
                        highlightbackground=COLOR)
clear_from_btn.pack(side=TOP, padx=5, pady=5)

clear_all_btn = Button(right, text="Clear All", font=("arial", 20, "bold"),
                       highlightbackground=COLOR)
clear_all_btn.pack(side=TOP, padx=5, pady=5)

send_btn = Button(right, text="Send", font=("arial", 20, "bold"),
                  highlightbackground=COLOR)
send_btn.pack(side=TOP, padx=5, pady=5)


# Define Entry and Labels in 'top' frame
from_label = Label(top, font=("arial", 20, "bold"), text="From: ", bg=COLOR)
from_label.place(x=10, y=10)

from_entry = Entry(top, font=("arial", 20, "bold"), width=25,
                   bd=BORDER_DEPTH, insertwidth=CURSOR_WIDTH)
from_entry.place(x=80, y=10)

to_label = Label(top, font=("arial", 20, "bold"), text="To: ", bg=COLOR)
to_label.place(x=410, y=10)

to_entry = Entry(top, font=("arial", 20, "bold"), width=25,
                 bd=BORDER_DEPTH, insertwidth=CURSOR_WIDTH)
to_entry.place(x=480, y=10)


# Define Message Box in 'left' frame
message = Text(left, font=("arial", 20, "bold"), width=55,
               insertwidth=CURSOR_WIDTH)
message.pack(side=LEFT)


# Execute  root window
root.mainloop()
