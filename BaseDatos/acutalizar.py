
import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET edad = 30 WHERE nombre = 'Antonio'")

conexion.commit()
conexion.close()