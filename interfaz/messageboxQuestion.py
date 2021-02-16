#tkinter- messagebox for realize a question

import tkinter
from tkinter import messagebox
raiz = tkinter.Tk()
raiz.title("My program")

#creating a widown for question o truth anithing


#define the fuction
def preguntar():
	resultado = tkinter.messagebox.askquestion("Titulo de la pregunta","¿Quieres borrar este fichero?")
	if(resultado =="yes"):
		print("Si quiero borrar este fichero")
	else:
		print("No quiero borrar este fichero")

botton = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
botton.pack()

raiz.mainloop()