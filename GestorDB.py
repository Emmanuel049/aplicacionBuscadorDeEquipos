#Clase diseñada con patrón de diseño Singleton

from importlib import import_module
from typing_extensions import Self

import psycopg2

host='localhost',
user='postgres',
password='felgrand97',
database='Project-Esport',
port=5432

class GestorDB:
    def __init__(self):
        self

    def iniciarConexion(self,host_,user_,password_,database_,port_):
        self.db = psycopg2.connect(
                host=host_,
                user=user_,
                password=password_,
                database=database_,
                port=port_
        )
        self.cursor = self.db.cursor()
        print("Conexion Exitosa")

    def ejecutar(self,query):
        self.cursor.execute(query)
        print("Query {} ejecutada con éxito".format(query))

    def mostrarResultados(self):
        return self.cursor.fetchall()

    def mostrarPrimerResultado(self):
        return self.cursor.fetchone()

    def finalizarConexion(self):
        self.db.close()
        print("Conexión Finalizada")

    def commit(self):
        self.db.commit()