import tkinter
from tkinter import *
from tkinter import ttk
from vistas.frame_carrera import *
from vistas.frame_materia import *
from vistas.frame_profesor import *
from vistas.frame_estudiante import *

class Aplication(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ventana = ventana

        self.ventana.title("sistema Universitario")
        self.ventana.iconbitmap("img/corona.ico")

        #Contenedor de Paneles

        self.navegador = ttk.Notebook(self)#declarando para crear los navegadores

        #Panel de Inicio
        self.inicio = Label(self.navegador, text = "pagina de inicio")
        self.navegador.add(self.inicio, text="Inicio")

        #Panel de carrera
        self.carrera = Vista_carrera(self.navegador)
        self.navegador.add(self.carrera, text="Carrera")

        #panel de materia
        self.materia = VistaMateria(self.navegador)
        self.navegador.add(self.materia, text="Materia")

        #panel de profesor
        self.profesor = VistaProfesor(self.navegador)
        self.navegador.add(self.profesor, text="Profesor")

        #panel de estudiante
        self.estudiante = VistaEstudiante(self.navegador)
        self.navegador.add(self.estudiante, text="Estudiante")


        self.navegador.pack()
        self.pack()


