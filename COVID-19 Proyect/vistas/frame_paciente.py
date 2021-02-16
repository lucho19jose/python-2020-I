from tkinter import *
from tkinter import ttk 
from conexion_db.consultas_db import *

class vista_paciente(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		def agregar_datos():
			query = 'INSERT INTO patient VALUES (NULL, ?, ?, ?, ?, ?, ?)'
			parametros = (self.entry_DNI.get(), self.entry_lastName.get(), self.entry_firstName.get(), self.entry_age.get(), self.entry_direction.get(), self.entry_symptoms.get())

			conn = Conectar_db()
			conn.run_db(query, parametros)
			#limpiar campos
#			self.entry_nombre.delete(0, END)
#			self.entry_duracion.delete(0, END)

			#actualiza la tabla
			listar_datos()




		#label titulo registrar
		self.label_titulo_registrar = Label(self, text = "Registrar Nuevo Paciente: ")
		self.label_titulo_registrar.grid(row = 0, column = 0, columnspan = 2, pady = 10,padx = 10)

		#Label y camp dni 
		self.label_DNI = Label(self, text = "Patient DNI: ")
		self.label_DNI.grid(row = 1, column = 0, pady = 10, padx = 10)

		self.entry_DNI = Entry(self, state = 'normal')
		self.entry_DNI.grid(row = 1, column = 1, pady = 10, padx = 10)

		self.entry_DNI.configure(bg='#F3F781')

		#Label y camp last name 
		self.label_lastName = Label(self, text = "Last Name: ")
		self.label_lastName.grid(row = 2, column = 0, pady = 10, padx = 5)

		self.entry_lastName = Entry(self, state = "normal")
		self.entry_lastName.grid(row = 2, column = 1, pady = 10, padx = 5)

		#Label y camp first name
		self.label_firstName = Label(self, text="First Name: ")
		self.label_firstName.grid(row = 3, column = 0, pady = 10, padx = 5)

		self.entry_firstName = Entry(self, state="normal")
		self.entry_firstName.grid(row = 3, column = 1, pady = 10, padx = 5)

		#Label y camp age
		self.label_age = Label(self, text = "Patient Age: ")
		self.label_age.grid(row = 4, column = 0, pady = 10, padx = 5)

		self.entry_age = Entry(self, state = "normal")
		self.entry_age.grid(row = 4, column = 1, pady = 10, padx = 5)

		#Label y camp direction
		self.label_direction = Label(self, text = "Direction: ")
		self.label_direction.grid(row = 5, column = 0, pady = 10, padx = 5)

		self.entry_direction = Entry(self, state = "normal")
		self.entry_direction.grid(row = 5, column = 1, pady = 10, padx = 5)

		#Label y camp symptoms
		self.label_symptoms = Label(self, text = "Patient symptoms: ")
		self.label_symptoms.grid(row = 6, column = 0, pady = 10, padx = 5)

		self.entry_symptoms = Entry(self, state = "normal")
		self.entry_symptoms.grid(row = 6, column = 1, pady = 10, padx = 5)


		#Boton Nuevo
		self.boton_nuevo = Button(self, text = "Nuevo")
		self.boton_nuevo.grid(row = 7, column= 0, pady = 10, padx = 10)

		#Boton Guardar
		self.boton_guardar = Button(self, text = "Guardar", command = agregar_datos)
		self.boton_guardar.grid(row = 7, column= 1, pady = 10, padx = 5)

		#label list of patients
		self.label_listaPaciente = Label(self, text = "List of Patients")
		self.label_listaPaciente.grid(row = 8, column = 1, pady = 10, padx = 10)

		#table

		self.table = ttk.Treeview(self, columns = ('', '',''))
		self.table.grid(row = 9, column = 0, columnspan = 9, pady = 10, padx = 10)
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

		#lack make module about conect patient and proof 






