import tkinter
from tkinter import messagebox
raiz = tkinter.Tk()
raiz.title("My prgram")

def avisar():
	tkinter.messagebox.showinfo("Titulo", "Mensaje con la informacion")


botton = tkinter.Button(raiz, text = "Pulsar para aviso", command=avisar)
botton.pack()

raiz.mainloop()