import sqlite3

conexion = sqlite3.connect("../db/coronas_tests.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM patient")

carreras = cursor.fetchall()

for carrera in carreras:
	print(carrera)

conexion.close()