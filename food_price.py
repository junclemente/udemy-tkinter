from tkinter import *

# Configure Window
root = Tk()
root.title("Food Price")
root.geometry("300x200")
root.resizable(width=False, height=False)
color = 'gray77'
root.configure(bg=color)

# Declare variables, IntVar() is tkinter variable declaration
BANANA = 5
APPLE = 7
ORANGE = 10
v = IntVar()
res = IntVar()


# Function that takes value from entry_2, calculates and updates res value
def cal_price():
    value = int(v.get())

    if value == 0:
        res.set(int(entry_2.get()) * BANANA)
    elif value == 1:
        res.set(int(entry_2.get()) * APPLE)
    elif value == 2:
        res.set(int(entry_2.get()) * ORANGE)
    else:
        pass


# Create text label at top of window
label = Label(root, text="Choose an Item", bg=color)
label.place(x=95, y=5)

# Create and label radio buttons
r_btn = Radiobutton(root, text="Banana", bg=color, variable=v, value=0)
r_btn.place(x=5, y=30)

r_btn2 = Radiobutton(root, text="Apple", bg=color, variable=v, value=1)
r_btn2.place(x=5, y=60)

r_btn3 = Radiobutton(root, text="Orange", bg=color, variable=v, value=2)
r_btn3.place(x=5, y=90)


# Create and label 'Price' entry box
entry = Entry(root, width=22, textvariable=res)
entry.place(x=80, y=130)

label_res = Label(root, text="Price", bg=color)
label_res.place(x=5, y=130)

# Create entry box and button that calls cal_price function
entry_2 = Entry(root, width=22)
entry_2.place(x=80, y=160)

btn = Button(root, text="Cal", highlightbackground=color,
             command=lambda: cal_price())
btn.place(x=5, y=160)


# Refreshes 'root' window and continues to run it
root.mainloop()
