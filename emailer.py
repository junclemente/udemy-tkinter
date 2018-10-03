from tkinter import *
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText


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


# Define Functions
def clear_from():
    from_entry.delete(0, END)


def clear_to():
    to_entry.delete(0, END)


def clear_all():
    clear_from()
    clear_to()


def send_email():

    HOST = 'smtp.gmail.com'
    PORT = 465

    USERNAME = 'email@address.com'  # Enter your email address
    PASSWORD = 'Passw0rd'  # Enter the Google provided password

    SENDER = from_entry.get()
    RECIPIENT = to_entry.get()

    text_subtype = 'plain'

    msg = MIMEText(message.get('1.0', END), text_subtype)

    msg['Subject'] = 'Python Script'
    msg['From'] = SENDER
    msg['To'] = RECIPIENT

    try:
        connection = SMTP(HOST, PORT)
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(SENDER, RECIPIENT, msg.as_string())
    except Exception as e:
        print(e)


# Define Frames
top = Frame(root, width=800, height=50, bg=COLOR)
top.pack(side=TOP)

bottom = Frame(root, width=800, height=50, bg=COLOR)
bottom.pack(side=BOTTOM)

left = Frame(root, width=600, height=400, bg=COLOR)
left.pack(side=LEFT)

right = Frame(root, width=200, height=400, bg=COLOR)
right.pack(side=RIGHT)


# Define buttons in 'right' frame
clear_to_btn = Button(right, text="Clear To", font=("arial", 20, "bold"),
                      highlightbackground=COLOR,
                      command=clear_to)
clear_to_btn.pack(side=TOP, padx=5, pady=5)

clear_from_btn = Button(right, text="Clear From", font=("arial", 20, "bold"),
                        highlightbackground=COLOR,
                        command=clear_from)
clear_from_btn.pack(side=TOP, padx=5, pady=5)

clear_all_btn = Button(right, text="Clear All", font=("arial", 20, "bold"),
                       highlightbackground=COLOR,
                       command=clear_all)
clear_all_btn.pack(side=TOP, padx=5, pady=5)

send_btn = Button(right, text="Send", font=("arial", 20, "bold"),
                  highlightbackground=COLOR,
                  command=send_email)
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
