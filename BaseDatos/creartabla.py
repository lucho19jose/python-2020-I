import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor() #crea un object for execute sentencias(query) en bd

cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER )")

conexion.commit()

conexion.close()
