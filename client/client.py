import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from loginPage import *

GUI = tk.Tk()
GUI.configure(bg = '#639c8f')
GUI.geometry('500x500')
GUI.title('Python Client')
GUI.resizable(False,False)
display_label1 = Label(GUI,text="Control Panel: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
display_label1.grid(row = 1, column = 0)

def moveRobot(direction):
    apiUrl = SERVER_URL + "move?direction=" + direction + "&turn=" + "0" + "&time=" + "0";
    response = requests.get(apiUrl)
    #if "success" == json.loads(response.text):
        #label_log.config(text = label_log.cget("text") +"\n"+ datetime.now().strftime("%Y-%m-%d %H:%M:%S") +" :" + user + " - moved the robot in the " +direction + " direction ")
    #else:
        #messagebox.showinfo("Error", response.text)   
       
def moveForward():
   msg = messagebox.showinfo("Robot Moved", "Forward")
forward = Button(text ="↑", command = moveForward)
forward.grid(row = 3, column = 1)
def moveLeft():
   msg = messagebox.showinfo("Robot Moved", "Left")
left = Button(text ="←", command = moveLeft)
left.grid(row = 5, column = 0)
def moveRight():
   msg=messagebox.showinfo("Robot Moved", "Right")
right = Button(text ="→", command = moveRight)
right.grid(row = 5, column = 2)
def moveBackward():
   msg=messagebox.showinfo("Robot Moved", "Backward")
backward = Button(text ="↓", command = moveBackward)
backward.grid(row = 8, column = 1)
def Start():
   msg = messagebox.showinfo("Robot", "Started")
start = Button(text ="🟢", command = Start)
start.grid(row = 4, column = 1)

start = Button(text ="")
start.grid(row = 5, column = 1)

def Stop():
   msg=messagebox.showinfo("Robot", "Stopped")
stop = Button(text ="🛑", command = Stop)
stop.grid(row = 6, column = 1)

display_label2 = Label(GUI,text="Log History: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
display_label2.grid(row = 15, column = 0)

display_label3 = Label(GUI,text="Video Feed: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
display_label3.grid(row = 1, column = 12)

display_label2 = Label(GUI,text="Blank Feed: ",bg = '#639c8f',fg='#e21d76',font = 'bold')
display_label2.grid(row = 15, column = 12)

blanklabel = Label(GUI, text = "", bg = '#639c8f',fg='#e21d76')
blanklabel.grid(row = 15, column = 12)

exit_button = tk.Button(GUI, text = 'Logout', bg='#A877BA',font = 'bold', command = GUI.destroy)
exit_button.grid(row = 20, column = 12)

GUI.mainloop()
