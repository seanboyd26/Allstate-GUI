from tkinter import *


username = "Sean"
password = "Password"
root = Tk()
root.title("Allstate LBL and Network ID Database GUI")
user_name = StringVar()
user_password = StringVar()


def authentication():

    if user_name.get() == username and user_password.get() == password:
        top = Toplevel()
        top.title("Login Successful",)
        top.geometry("200x100-400+300")
        msg = Message(top, text="\n\nAuthenticated")
        msg.config(anchor=CENTER, aspect=200)
        msg.pack()
        button = Button(top, text="Proceed", command=top.destroy)
        button.pack()
        root.destroy()
        new_root()

    elif user_name.get() == username and user_password.get() != password:
        top = Toplevel()
        top.title("User login status")
        top.geometry("200x100-400+300")
        msg = Message(top, text="Invalid Credentials")
        msg.pack()
        button = Button(top, text="Re-try", command=top.destroy, anchor=W)
        button.pack()


def new_root():
    root1 = Tk()
    root1.geometry("200x100-400+300")
    root1.title("Allstate GUI")
    label1 = Label(root1, fg="red", font=("Helvetica", 12), text="Welcome " + user_name.get())
    label1.grid(row=0, column=0)
    title1_img = PhotoImage(file="C:/Users/sboye/Desktop/allstate.gif")
    root1.tk.call("wm", "iconphoto", root1._w, title1_img)


def logout():
    """When user clicks logout this will call root destroy."""
    top = Toplevel()
    top.title("User logout")
    top.geometry("200x100-400+300")


def about():
    """This will display information about the program version and author etc"""


menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
file_menu.add_command(label="Logout", command=logout)
menu.add_cascade(label="File", menu=file_menu)
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")
logo = PhotoImage(file="C:/Users/sboye/Desktop/allstate.gif")
title_img = PhotoImage(file="C:/Users/sboye/Desktop/allstate.gif")
root.tk.call("wm", "iconphoto", root._w, title_img)
label2 = Label(root, image=logo)
label2.grid()
usr_lbl = Label(root, text="Username: ")
usr_lbl.grid()
e = Entry(root, textvariable=user_name)
e.grid(sticky=S)
psw_lbl = Label(root, text="Password: ")
psw_lbl.grid()
e1 = Entry(root, textvariable=user_password, show="*")
e1.grid(sticky=S)
button1 = Button(root, text="Submit", command=authentication)
button1.grid()


root.mainloop()
