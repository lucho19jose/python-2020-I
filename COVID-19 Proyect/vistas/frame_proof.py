from tkinter import *
from tkinter import ttk 
from conexion_db.consultas_db import *

class Vista_Proof(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#Label y camp dni 
		self.label_DNI = Label(self, text = "Patient DNI: ")
		self.label_DNI.grid(row = 1, column = 0, pady = 10, padx = 10)

		self.entry_DNI = Entry(self, state = 'normal')
		self.entry_DNI.grid(row = 1, column = 1, pady = 10, padx = 10)

		self.entry_DNI.configure(bg='#F3F781')

		#Label y camp last name 
		self.label_lastName = Label(self, text = "Last Name: ")
		self.label_lastName.grid(row = 1, column = 2, pady = 10, padx = 5)

		self.entry_lastName = Entry(self, state = "normal")
		self.entry_lastName.grid(row = 1, column = 3, pady = 10, padx = 5)

		#Label y camp search person
		self.label_search = Label(self, text = "Search: ")
		self.label_search.grid(row = 1, column = 6, pady = 5, padx = 5)

		self.entry_search = Entry(self, state = "normal")
		self.entry_search.grid(row = 1, column = 7, pady = 5, padx = 5)

		#table

		self.table = ttk.Treeview(self, columns = ('', '',''))
		self.table.grid(row = 2, column = 4, columnspan = 9, pady = 10, padx = 10)
		self.table.heading('#0', text = "Code Patient")
		self.table.heading('#1', text = "DNI")
		self.table.heading('#2', text = "Name")
		self.table.heading('#3', text = "Age")



		def listar_datos():

			#Eliminar datos de la tabla
			recorrer_tabla = self.table.get_children()
			for elementos in recorrer_tabla:
				self.table.delete(elementos)

			query = """SELECT id_patient, dni, last_name ||' '||first_name as "Name", age FROM patient"""
			conn = Conectar_db()
			datos = conn.run_db(query)

			for patient in datos:
				self.table.insert('',0,text = patient[0], value = (patient[1],patient[2],patient[3]))

		#Listar datos en la tabla
		listar_datos()