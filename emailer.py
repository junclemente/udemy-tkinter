from tkinter import *


# Define static variables
COLOR = 'gray55'

# Define root window
root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)
root.title("Email Sender")
root.configure(bg=COLOR)


# Define Frames
top = Frame(root, width=800, height=50, bg="black")
top.pack(side=TOP)

bottom = Frame(root, width=800, height=50, bg="red")
bottom.pack(side=BOTTOM)

left = Frame(root, width=600, height=400, bg="blue")
left.pack(side=LEFT)

right = Frame(root, width=200, height=400, bg=COLOR)
right.pack(side=RIGHT)


# Define buttons
clear_to_btn = Button(right, text="Clear To", font=('arial', 20, 'bold'),
                      highlightbackground=COLOR)
clear_to_btn.pack(side=TOP, padx=5, pady=5)

clear_from_btn = Button(right, text="Clear From", font=('arial', 20, 'bold'),
                      highlightbackground=COLOR)
clear_from_btn.pack(side=TOP, padx=5, pady=5)

clear_all_btn = Button(right, text="Clear All", font=('arial', 20, 'bold'),
                      highlightbackground=COLOR)
clear_all_btn.pack(side=TOP, padx=5, pady=5)

send_btn = Button(right, text="Send", font=('arial', 20, 'bold'),
                      highlightbackground=COLOR)
send_btn.pack(side=TOP, padx=5, pady=5)


# Execute  root window
root.mainloop()