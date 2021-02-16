
import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

lista_personas = [('Pedro', 'Rodriguez', 'Perez',26),('Maria', 'Lopez', 'Gomez',48),
('Luis', 'Barboza', 'Juanma',12)]


cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas) #introducir una lista de valores

conexion.commit()

conexion.close()	