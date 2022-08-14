# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 13:19:34 2022

@author: Mauro
"""

from cmath import log
from distutils.log import Log
from GestorDB import GestorDB
from GestorLogin import GestorLogin

#import psycopg2

CONEXION_LOGIN = GestorLogin()



def sign_in(mail, pwd):
    #compara los usuarios con la BD y si no estan los rechaza.

    CONEXION_LOGIN.sign_in(mail,pwd)

def sign_up(mail,pwd):

    CONEXION_LOGIN.sign_up(mail,pwd)

def Test_Login(mail,pwd):
    print (sign_in(mail,pwd))


def Test_Register(mail,pwd):
    print (sign_up(mail,pwd))

# Test_Login('usuariodeprueba@gmail.com',"prueba12345")
# Test_Register('prueba_evelyn@gmail.com.ar',"ekisdexD")
