import tkinter.messagebox
from tkinter import *


# Declare static variables
COLOR = "gray55"
COLOR2 = "gray88"


# Define main window
root = Tk()
root.geometry("400x150")
root.resizable(width=False, height=False)
root.title("Simple Calculator")
root.configure(bg=COLOR)

# Declare Tk variables
num1 = IntVar()
num2 = IntVar()
result_value = IntVar()

# Define frames
top_frame = Frame(root, width=400, height=40, bg=COLOR)
top_frame.pack(side=TOP)

top2_frame = Frame(root, width=400, height=40, bg=COLOR)
top2_frame.pack(side=TOP)

top3_frame = Frame(root, width=400, height=40, bg=COLOR)
top3_frame.pack(side=TOP)

bottom_frame = Frame(root, width=400, height=40, bg=COLOR)
bottom_frame.pack(side=TOP)


# Define functions
def errorMsg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror("Error!", "Something went really wrong. ")
    elif msg == 'divisionerror':
        tkinter.messagebox.showerror("Division Error!",
                                     "Cannot divide by 0. ")


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        result_value.set(value)

    except:
        errorMsg('error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        result_value.set(value)
    except:
        errorMsg('error')


def multiply():
    try:
        value = float(num1.get()) * float(num2.get())
        result_value.set(value)

    except:
        errorMsg('error')


def divide():

    if num2.get() == '0':
        errorMsg('divisionerror')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            result_value.set(value)

        except:
            errorMsg('error')


# Define buttons
btn_plus = Button(top3_frame, text=" + ", width=8,
                  highlightbackground=COLOR, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=5, pady=5)

btn_minus = Button(top3_frame, text=" - ", width=8,
                   highlightbackground=COLOR, command=lambda: minus())
btn_minus.pack(side=LEFT)

btn_multiply = Button(top3_frame, text=" * ", width=8,
                      highlightbackground=COLOR, command=lambda: multiply())
btn_multiply.pack(side=LEFT)

btn_divide = Button(top3_frame, text=" / ", width=8,
                    highlightbackground=COLOR, command=lambda: divide())
btn_divide.pack(side=LEFT)


# Define Entry and Labels
label_first_num = Label(top_frame, text="Input Number 1:", bg=COLOR)
label_first_num.pack(side=LEFT, padx=5, pady=5)

entry_first_num = Entry(top_frame, highlightbackground=COLOR,
                        textvariable=num1)
entry_first_num.pack(side=LEFT)

label_second_num = Label(top2_frame, text="Input Number 2:", bg=COLOR)
label_second_num.pack(side=LEFT, padx=5, pady=5)

entry_second_num = Entry(top2_frame, highlightbackground=COLOR,
                         textvariable=num2)
entry_second_num.pack(side=LEFT)


# Define Result box and labels
label_result = Label(bottom_frame, text="Result:", bg=COLOR)
label_result.pack(side=LEFT, padx=5, pady=5)

entry_result = Entry(bottom_frame, highlightbackground=COLOR,
                     textvariable=result_value)
entry_result.pack(side=LEFT)

# Execute window and refresh
root.mainloop()
