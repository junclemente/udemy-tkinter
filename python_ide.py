import tkinter.messagebox
from tkinter import *
from io import StringIO

# Declare variables
COLOR = "gray"
COLOR2 = "gray88"

# Define window
root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)
root.title("Run Python Code")
root.configure(bg=COLOR)


# Define functions
def clear_python():
    python_code.delete('1.0', END)


def run():
    # Listener for output, waiting for code to run
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()

    # Execute input from python_code textbox
    exec(python_code.get('1.0', END))
    sys.stdout = old_stdout

    # Gets result of 'redirected_output' and outputs into a messagebox
    tkinter.messagebox.showinfo('Result', redirected_output.getvalue())


# Define frames
top = Frame(root, width=800, height=50, bg=COLOR)
top.pack(side=TOP)

bottom = Frame(root, width=800, height=450, bg=COLOR)
bottom.pack(side=BOTTOM)

# Define buttons
btn_clear = Button(top, text="clear", highlightbackground=COLOR,
                   font=('arial', 25, 'bold'),
                   command=lambda: clear_python())
btn_clear.pack(side=TOP)

btn_run = Button(top, text="run", highlightbackground=COLOR,
                 font=('arial', 25, 'bold'),
                 command=lambda: run())
btn_run.pack(side=TOP)

# Define text box
python_code = Text(bottom, font=('arial', 25, 'bold'), bg=COLOR2)
python_code.pack(side=TOP)


root.mainloop()
