from tkinter import *
from tkinter import ttk

root = Tk()

#menu_frame = ttk.Frame(root)
#menu_frame.grid(column=0, row=0, sticky="n,w")

#main_frame = ttk.Frame(root)
#main_frame.grid(column=1, row=0, sticky="n")

Grid.columnconfigure(root,0,weight=1)
Grid.rowconfigure(root,(0,1),weight=1)


button1 = ttk.Button(root,text="Button 1")
button1.grid(column=0, row=0, sticky="nsew")
button2 = ttk.Button(root,text="Button 2")
button2.grid(column=0, row=1, sticky="nsew")


#button6 = ttk.Button(main_frame,text="OTHER BUTTON")
#button6.grid(column=1, row=0)





root.mainloop()