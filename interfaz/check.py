import tkinter

raiz = tkinter.Tk()
raiz.title("Hola")

def verificar():
	valor = check1.get()
	if valor == 1:
		print("El check esta activado")
	else:
		print("El check esta desactivado")


check1 = tkinter.IntVar()

boton1 = tkinter.Checkbutton(raiz, text="Option 1", variable = check1, onvalue=1, offvalue=0, command=verificar)
boton1.pack()

raiz.mainloop()