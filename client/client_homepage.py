import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import main
import clientGUI
import homePage

clientLogin = tk.Tk()
clientLogin.configure(bg = '#639c8f')
clientLogin.geometry('500x500')
clientLogin.title('Python Client')
clientLogin.resizable(False,False)

e1 = StringVar()
e2 = StringVar()

username = Label(clientLogin,text="Enter your username: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
username.grid(row = 0, column = 0)

password = Label(clientLogin,text="Enter your password: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
password.grid(row = 1, column = 0)

username = Entry(clientLogin,textvariable = e1)
username.grid(row = 0, column = 1)

password = Entry(clientLogin,textvariable = e2)
password.grid(row = 1, column = 1)

def save():
  e1.get()
  e2.get()

save_everything = Button(clientLogin,text="Save",command=save, bg='#fcba03',font = 'bold')
save_everything.grid(row = 500, column = 0)

logout = tk.Button(clientLogin, text = 'Logout', bg='#A877BA',font = 'bold', command = clientLogin.destroy)
clientLogin.grid(row = 20, column = 12)

clientLogin.mainloop()
