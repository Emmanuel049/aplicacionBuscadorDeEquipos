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

DICC_BD = dicc_bd(); 
def sign_in():
    #compara los usuarios con la BD y si no estan los rechaza.
    log = True;
    usuario = input("Ingrese usuario: ");
    if usuario in DICC_BD:
        contraseña = input("Ingrese contraseña: ");
        if contraseña == DICC_BD[usuario]:
            print("Logeaste con exito!")
        else:
            print("Contraseña incorrecta, ingrese nuevamente la contraseña")
            log = False
    else:
        print("Usuario incorrecto, ingrese nuevamente el usuario")
        log = False
    return log

def sign_up():
    #Ingresa datos para armar un usuario y guardarlo en la BD.
    nombre = input("Ingrese nombre: ");
    apellido = input("Ingrese apellido: ");
    usuario = input("Ingrese email: ");
    if usuario in DICC_BD:
        print("El usuario ya existe, vuelva a intentarlo."); 
        bandera = False
    else: 
        contraseña = input("Ingrese contraseña: ");
        DICC_BD[usuario] = contraseña
        bandera = True
    return bandera;

def dicc_bd():
    otro = 's';
    diccUsuarios = {};
    while (otro == 's'):
       usuario = input("Ingrese usuario: ");
       diccUsuarios[usuario] = input("Ingrese contraseña: ");
       otro = input("Ingrese s/n dependiendo si quiere o no seguir respectivamente: ");
    print(diccUsuarios);
    return diccUsuarios


def Main():
    cont = 0
    boolean = sign_up();
    print(DICC_BD)
    print(boolean)
Main();