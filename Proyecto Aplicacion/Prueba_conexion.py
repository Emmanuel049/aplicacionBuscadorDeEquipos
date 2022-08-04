# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 13:19:34 2022
@author: Mauro
"""
"""
def carga_dicc():
    #Carga el dicc con usuarios y contraseñas
    
    dicc_usuarios: 
        {
        "Usuario": " ",
        "Contraseña": " ",
        }
    
"""

from cmath import log
from distutils.log import Log
import psycopg2

def sign_in(mail, pwd):
    #compara los usuarios con la BD y si no estan los rechaza.

    try:
        db = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123CrackeN',
            database='postgres',
            port=8000
    )

        print("Conexion Exitosa")

        #Muestra el tipo y versión de la base de datos utilizada, se ejecuta en forma de prueba

        cursor = db.cursor()
        query = "SELECT version()"
        cursor.execute(query)
        retorno = cursor.fetchone()
        print(retorno)

        #Sentencias para encontrar la contraseña, en caso de no encontrarla 

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

def sign_up(registerEmail,registerPassword):

    try:
        db = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123CrackeN',
            database='postgres',
            port=8000
        )

        print("Conexion Exitosa")

        #Muestra el tipo y versión de la base de datos utilizada, se ejecuta en forma de prueba

        cursor = db.cursor()
        query = "SELECT version()"
        cursor.execute(query)
        retorno = cursor.fetchone()
        print(retorno)

        #Sentencias para revisar que no exista el usuario, ya que no puedo ingresar un usuario que ya existe

        query = "SELECT email FROM login WHERE email LIKE '{}'".format(registerEmail)
        print(query)
        cursor.execute(query)
        retorno = cursor.fetchall()
        print(retorno)

        if (len(retorno) != 0):
            raise Exception("No puedo crear una cuenta con un usuario con mail ya existente en la base de datos")

        query = "INSERT INTO login (email, contraseña) VALUES ('{}','{}')".format(registerEmail,registerPassword)
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

def Test_Login(mail,pwd):
    print (sign_in(mail,pwd))


def Test_Register(registerEmail,registerPassword):
    print (sign_up(registerEmail,registerPassword))

# Test_Login('usuariodeprueba@gmail.com',"prueba12345")
# Test_Register('prueba_evelyn@gmail.com.ar',"ekisdexD")