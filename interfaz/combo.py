import tkinter
from tkinter import *
from tkinter import ttk

#No te sientas muy alegre de ningun logro o tampoco de las caidas
raiz = tkinter.Tk()
raiz.title("My program")

A = ["Sistemas", "Programacion", "Redes", "IA"]

ad = ttk.Combobox(raiz, state="readonly")
ad.grid(row=1, column=5,padx=10,pady=10)
ad['values'] = ("Systems", "Progaming", "Redes") 
ad.set("SELECT ANYTHING")
ad.current(newindex=2)
raiz.mainloop()