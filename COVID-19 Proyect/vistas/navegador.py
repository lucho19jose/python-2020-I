import tkinter
from tkinter import *
from tkinter import ttk
from vistas.frame_paciente import *
from vistas.frame_proof import *
class Aplication(ttk.Frame):
	def __init__(self, ventana):
		super().__init__(ventana)

		self.ventana = ventana
		self.ventana.title("Registre corona")
		self.ventana.iconbitmap("img/corona.ico")
		self.ventana.configure(bg='#81DAF5')

		#contenedor de paneles
		self.navegador = ttk.Notebook(self)

		#Panel de Inicio
		self.inicio = Label(self.navegador, text = "pagina de inicio")
		self.navegador.add(self.inicio, text="INICIO")

		#Panel pacientes
		self.paciente = vista_paciente(self.navegador)
		self.navegador.add(self.paciente, text ="Paciente")

		#Panel prueba
		self.proof = Vista_Proof(self.navegador)
		self.navegador.add(self.proof, text = "proof")

		#Panel de resultados


		self.navegador.pack()
		self.pack()