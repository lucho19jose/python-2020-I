
import tkinter
raiz = tkinter.Tk() 
raiz.title("My first program")

def action():
	print("hi boos")


boton = tkinter.Button(raiz, text ="Ejecutar", command = action)
boton.pack()

raiz.mainloop()
