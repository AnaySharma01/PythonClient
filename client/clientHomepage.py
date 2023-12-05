import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from clientLogin import *
from clientRegistration import *

def loginFunction():
    loginWindow()
    
def registrationFunction():
    registrationWindow()

root = tk.Tk() 
root.configure(bg = '#639c8f')
root.geometry('500x500')
root.title('Python Client')
root.resizable(False,False)

register = Button(text ="Registration", command = registrationFunction)
register.grid(row = 1, column = 1)

loginbtn = Button(text ="Login", command = loginFunction)
loginbtn.grid(row = 3, column = 1)

exit_button = Button(root, text = 'Exit', bg='#A877BA',font = 'bold', command = root.destroy)
exit_button.grid(row = 20, column = 12)

root.mainloop()


