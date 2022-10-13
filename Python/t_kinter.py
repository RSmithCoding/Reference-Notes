# Notes on using Tkinter and any extension libarys to it

from tkinter import *        # Core tkinter  
from tkinter import ttk
from turtle import width         # Allows to use widgets


root = Tk()                # Creates a tk object window called root
root.title("Test Program")  # Title of window

#root.geometry("800x600")           # Sets the height and width of the app

# Below sets the app size and centers it on the screen

app_width = 800
app_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}') 

frame = ttk.Frame(root, padding="3 3 10 10")
frame.grid(column=0,row=0, sticky="N,W,E,S")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

Grid.rowconfigure(frame, 2, weight=1)



ttk.Button(frame,text="Press Me!").grid(column=2,row=2)






root.mainloop()     # Calls the mainloop in tk to run the program