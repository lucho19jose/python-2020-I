import tkinter
from tkinter import *
from tkinter import ttk
from vistas.navegador import *

if __name__ == '__main__':
	ventana = Tk()

	app = Aplication(ventana)
	ventana.configure(bg='#81DAF5')

	ventana.mainloop()