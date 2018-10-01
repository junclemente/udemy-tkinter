from tkinter import *

# Configure Window
root = Tk()
root.title("Food Price")
root.geometry("300x200")
root.resizable(width=False, height=False)
root.configure(bg='gray77')


label = Label(root, text="Choose an Item")
label.place(x=95, y=5)

r_btn = Radiobutton(root, text="Banana")
r_btn.place(x=5, y=30)

r_btn2 = Radiobutton(root, text="Apple")
r_btn2.place(x=5, y=60)

r_btn3 = Radiobutton(root, text="Orange")
r_btn3.place(x=5, y=90)


entry = Entry(root, width=22)
entry.place(x=80, y=130)

label_res = Label(root, text="Price")
label_res.place(x=5, y=130)

entry_2 = Entry(root, width=22)
entry_2.place(x=80, y=160)

btn = Button(root, text="Cal")
btn.place(x=5, y=160)

# Refreshes 'root' window and continues to run it
root.mainloop()
