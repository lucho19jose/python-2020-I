import tkinter

raiz = tkinter.Tk()
raiz.title("my program")

def selection():
	print("the option selected is {}".format(option.get()))


option = tkinter.IntVar()

botonradio1 = tkinter.Radiobutton(raiz, text = "Option1", variable = option, value=1, command=selection)
botonradio1.pack()
 
botonradio2 = tkinter.Radiobutton(raiz, text = "Option2", variable = option, value=2, command=selection)
botonradio2.pack()

botonradio3 = tkinter.Radiobutton(raiz, text = "Option3", variable = option, value=3, command=selection)
botonradio3.pack()


raiz.mainloop()