import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import main
import clientGUI
import homePage

clientHomepage = tk.Tk()
clientHomepage.configure(bg = '#639c8f')
clientHomepage.geometry('500x500')
clientHomepage.title('Python Client')
clientHomepage.resizable(False,False)

e1 = StringVar()
e2 = StringVar()

username = Label(clientHomepage,text="Enter your username: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
username.grid(row = 0, column = 0)

password = Label(clientHomepage,text="Enter your password: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
password.grid(row = 1, column = 0)

username = Entry(clientHomepage,textvariable = e1)
username.grid(row = 0, column = 1)

password = Entry(clientHomepage,textvariable = e2)
password.grid(row = 1, column = 1)

def save():
  e1.get()
  e2.get()

save_everything = Button(clientHomepage,text="Save",command=save, bg='#fcba03',font = 'bold')
save_everything.grid(row = 500, column = 0)

logout = tk.Button(clientHomepage, text = 'Logout', bg='#A877BA',font = 'bold', command = clientHomepage.destroy)
clientHomepage.grid(row = 20, column = 12)

clientHomepage.mainloop()
