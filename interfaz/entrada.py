
import tkinter 

raiz = tkinter.Tk()
raiz.title("My program")

#creating our components entry(Enter dates)
frame = tkinter.Frame(raiz)
frame.config(height=400, width=300)
frame.pack()
entrada = tkinter.Entry(raiz)
entrada.config(justify="center", show="*")
entrada.pack()

raiz.mainloop()