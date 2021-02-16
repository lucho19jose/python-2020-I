
import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS WHERE edad BETWEEN 18 AND 38 ")

personas = cursor.fetchall()

for persona in personas:
	print(persona)

conexion.close()
