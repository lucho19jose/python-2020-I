#creating bd basededatos.db

import sqlite3

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PRODUCTOS (id number, nombre TEXT, precio INT )")

lista_productos = [(1,"Impresora",300), (2,"Raton",20),(3,"Ordenador",600)]

cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", lista_productos)

conexion.commit()
conexion.close()