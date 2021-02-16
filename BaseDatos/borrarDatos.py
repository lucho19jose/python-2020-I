
import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()


cursor.execute("DELETE FROM PERSONAS WHERE nombre='Pedro'")

conexion.commit()

conexion.close()