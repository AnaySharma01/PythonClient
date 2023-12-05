import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

root = tk.Tk()
root.configure(bg = '#639c8f')
root.geometry('500x500')
root.title('Python Client')
root.resizable(False,False)

e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()

fname = Label(root,text="Enter your first name: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
fname.grid(row = 0, column = 0)

lname = Label(root,text="Enter your last name: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
lname.grid(row = 1, column = 0)

username = Label(root,text="Enter your username: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
username.grid(row = 0, column = 0)

password = Label(root,text="Enter your password: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
password.grid(row = 1, column = 0)

username = Entry(root,textvariable = e1)
username.grid(row = 0, column = 1)

password = Entry(root,textvariable = e2)
password.grid(row = 1, column = 1)

def save():
  e1.get()
  e2.get()
  e3.get()
  e4.get()

save_everything = Button(root,text="Save",command=save, bg='#fcba03',font = 'bold')
save_everything.grid(row = 500, column = 0)


root.mainloop()
