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
        msg = Message(top, text="Invalid Password")
        msg.pack()
        button = Button(top, text="Re-try", command=top.destroy, anchor=W)
        button.pack()

    elif user_name.get() != username and user_password.get() == password:
        top = Toplevel()
        top.title("User login status")
        top.geometry("200x100-400+300")
        msg = Message(top, text="Invalid Username")
        msg.pack()
        button = Button(top, text="Re-try", command=top.destroy, anchor=W)
        button.pack()

    else:
        top = Toplevel()
        top.title("User login status")
        top.geometry("200x100-400+300")
        msg = Message(top, text="Invalid Username & Password")
        msg.pack()
        button = Button(top, text="Re-try", command=top.destroy, anchor=W)
        button.pack()


def new_root():
    """New root window function, this will be called after user logs in"""
    root1 = Tk()
    root1.geometry("200x100-400+300")
    root1.title("Welcome, " + user_name.get())
    r_bttn = Radiobutton(root1, value=1, text="Search for user")
    r_bttn.grid(row=0, column=1)
    entry = Entry(root1)
    entry.grid(row=1, column=1)
    r_bttn1 = Radiobutton(root1, value=2, text="Delete a user")
    r_bttn1.grid(row=2, column=1)
    entry1 = Entry(root1)
    entry1.grid(row=3, column=1)
    title1_img = PhotoImage(file="C:/Users/sboye/Desktop/AllstateIcon.gif")
    root1.tk.call("wm", "iconphoto", root1._w, title1_img)
    button = Button(root1, text="Submit")
    button.grid(row=5, column=1)
    text = Text(root1, width=20, height=5)
    text.grid(row=6, column=1)


def logout():
    """When user clicks logout this will call root destroy."""
    top = Toplevel()
    top.title("User logout")
    top.geometry("200x100-400+300")
    label = Label(top, text="Are you sure you want to logout?")
    label.pack()
    button = Button(top, text="Yes", anchor=E, command=root.destroy)
    button.pack()
    button2 = Button(top, text="No", anchor=W, command=top.destroy)
    button2.pack()


def about():
    """This will display information about the program version and author etc"""
    top = Toplevel()
    top.title("About..")
    top.geometry("200x100-400+300")
    msg = Message(top, text="This program is in BETA testing and is not fully complete \
                        \nProgrammed by: \nSean Boyd")
    msg.pack()

menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
file_menu.add_command(label="Logout", command=logout)
menu.add_cascade(label="File", menu=file_menu)
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)
logo = PhotoImage(file="C:/Users/sboye/Desktop/allstate.gif")
title_img = PhotoImage(file="C:/Users/sboye/Desktop/AllstateIcon.gif")
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
