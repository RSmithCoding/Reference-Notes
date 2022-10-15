
from typing import MutableSequence
import customtkinter
from tkinter import *
from tkinter import ttk

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1920x1080")

menu = ttk.Frame(app)



Grid.columnconfigure(app,0,weight=1)
Grid.rowconfigure(app,(0,1),weight=1)


def resize(e):
    size = e.width / 10
    #button.text_font=("Roboto Medium",{size})
    #button2.text_font=("Roboto Medium",{size})
    

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(menu, text="Button")
button2 = customtkinter.CTkButton(menu,text="Button 2")


#button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

button.grid(column=0, row=0, sticky="nsew")
button2.grid(column=0, row=1, sticky="nsew")


app.bind('<Configure>',resize)



app.mainloop()