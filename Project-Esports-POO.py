from importlib import import_module
from typing_extensions import Self

import psycopg2

class interfaz:
    #va a ser el esqueleto de los datos pedidos
    def __init__(self,usuario, pwd):
        self.usuario= usuario
        self.pwd = pwd

    def sign_in(self, mail, pwd):
    #compara los usuarios con la BD y si no estan los rechaza.

        try:
            db = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='felgrand97',
                database='Project-Esport',
                port=5432
            )
            cursor = db.cursor()
            query = "SELECT contraseña FROM login WHERE email LIKE '{}'".format(mail)
            print(query)
            cursor.execute(query)
            retorno = cursor.fetchall()
            print(retorno)

            if (len(retorno) == 0):
                raise Exception("No encontré el mail solicitado en la base de datos")

            if (retorno[0][0] != pwd):
                raise Exception("La contraseña ingresada no coincide")
            
            print(type(retorno))
            print(retorno)

            respuesta = True

        except Exception as e:
            print (e)
            respuesta = False

        finally:
            db.close()
            print("Conexion Finalizada")
            print("Devolviendo respuesta: {}".format(respuesta))
            return respuesta



    def sign_up(self, mail, pwd):

        try:
            db = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='asd123',
                database='postgres',
                port=1234
            )

            print("Conexion Exitosa")

            #Muestra el tipo y versión de la base de datos utilizada, se ejecuta en forma de prueba

            cursor = db.cursor()
            query = "SELECT version()"
            cursor.execute(query)
            retorno = cursor.fetchone()
            print(retorno)

            #Sentencias para revisar que no exista el usuario, ya que no puedo ingresar un usuario que ya existe

            query = "SELECT email FROM login WHERE email LIKE '{}'".format(mail)
            print(query)
            cursor.execute(query)
            retorno = cursor.fetchall()
            print(retorno)

            if (len(retorno) != 0):
                raise Exception("No puedo crear una cuenta con un usuario con mail ya existente en la base de datos")

            query = "INSERT INTO login (email, contraseña) VALUES ('{}','{}')".format(mail,pwd)
            print(query)
            cursor.execute(query)
            db.commit()
            respuesta = True

        except Exception as e:
            print (e)
            respuesta = False

        finally:
            db.close()
            print("Conexion Finalizada")
            print("Devolviendo respuesta: {}".format(respuesta))
            return respuesta

'''
def Test_Login(mail,pwd):
    print (sign_in(mail,pwd))


def Test_Register(mail,pwd):
    print (sign_up(mail,pwd))
'''