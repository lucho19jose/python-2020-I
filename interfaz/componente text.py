import tkinter

raiz = tkinter.Tk()
raiz.title("My program...")

#create our components text (tex long many lines)

entrada = tkinter.Text(raiz)
entrada.config(width = 30, height=10, font=("Verdana", 15), padx=10, pady = 10, fg="green", selectbackground="lightgrey")
entrada.pack()

raiz.mainloop()

