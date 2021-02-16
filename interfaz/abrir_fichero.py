import tkinter
from tkinter import filedialog
raiz = tkinter.Tk()
raiz.title("My program")

#definir abrirfichero

def abrirfichero():
	rutafichero = filedialog.askopenfilename(title="Abrir un fichero")
	print(rutafichero)

boton = tkinter.Button(raiz, text="Pulsa para empezar", command=abrirfichero)
boton.pack()

raiz.mainloop()