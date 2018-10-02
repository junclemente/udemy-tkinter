from tkinter import *


# Declare variables
COLOR = "gray55"
COLOR2 = "gray88"

# Define main window
root = Tk()
root.geometry("400x150")
root.resizable(width=False, height=False)
root.title("Simple Calculator")
root.configure(bg=COLOR)

# Define frames
top_frame = Frame(root, width=400, height=40, bg=COLOR)
top_frame.pack(side=TOP)

top2_frame = Frame(root, width=400, height=40, bg=COLOR)
top2_frame.pack(side=TOP)

top3_frame = Frame(root, width=400, height=40, bg=COLOR)
top3_frame.pack(side=TOP)

bottom_frame = Frame(root, width=400, height=40, bg=COLOR)
bottom_frame.pack(side=TOP)

# Define buttons
btn_plus = Button(top3_frame, text=" + ", width=8, highlightbackground=COLOR)
btn_plus.pack(side=LEFT, padx=5, pady=5)

btn_minus = Button(top3_frame, text=" - ", width=8, highlightbackground=COLOR)
btn_minus.pack(side=LEFT)

btn_multiply = Button(top3_frame, text=" * ", width=8, highlightbackground=COLOR)
btn_multiply.pack(side=LEFT)

btn_divide = Button(top3_frame, text=" / ", width=8, highlightbackground=COLOR)
btn_divide.pack(side=LEFT)

# Execute window and refresh
root.mainloop()