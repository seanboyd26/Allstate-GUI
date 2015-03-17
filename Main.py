from tkinter import *

root = Tk()
root.title("ALLSTATE NTID/LBL SOFTWARE - SEAN BOYD")
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
file_menu.add_command(label = "Logout")
menu.add_cascade(label = "File", menu= file_menu)
edit_menu = Menu(menu)
menu.add_cascade(label = "Edit", menu = edit_menu)
help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label = "About")
label1 = Label(root, text="Allstate NTID/LBL Application")
label1.grid(row=0, column=0)
logo = PhotoImage(file="C:/Users/sboye/Desktop/allstate.gif")
label2 = Label(root, image=logo)
label2.grid()
usr_lbl = Label(root, text = "Username: ")
usr_lbl.grid()
e= Entry(root)
e.grid(sticky = S)
e.insert(0, " ")
psw_lbl = Label(root, text = "Password: ")
psw_lbl.grid()
e1= Entry(root, show="*")
e1.grid(sticky = S)
e1.insert(0, "Password: ")


class Program:
    def __init__(self):
        button1 = Button(root, text = "Submit",  command=self.callback)
        button1.grid()


    def callback(self):
        top = Toplevel()
        top.title("User login status")
        top.geometry("200x100-400+300")
        msg = Message(top, text = "Logging in..")
        msg.pack()
        button = Button(top, text ="Proceed", command = top.destroy)
        button.pack()


Program()
root.mainloop()

