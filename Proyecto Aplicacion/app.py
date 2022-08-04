#---------------------------------- FLASK --------------------------------------

from flask import Flask, render_template, url_for, request,redirect
import forms
from cmath import log
from distutils.log import Log
import Prueba_conexion
from register import RegistrationForm


app = Flask(__name__)
# clase a ejecutar para obtener la coneccion, con parametro __name__

#---------------------------------- Rutas Registro / Login  --------------------------------------

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm(request.form)
    if request.method == 'POST' and register_form.validate():
        registerEmail = register_form.email.data
        registerPassword = register_form.password.data
        print(registerEmail + "  " + registerPassword)
        respuestaRegistro = Prueba_conexion.sign_up(registerEmail,registerPassword)
        print("La respuesta es: " + str(respuestaRegistro))
        if respuestaRegistro == True:
            return redirect(url_for('Login'))
    return render_template('register.html', form=register_form)

@app.route("/login", methods = ['GET','POST'])
def Login():
    login_form = forms.LogginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        mail = login_form.username.data
        pwd = login_form.password.data
        print(mail,pwd)
        respuesta = Prueba_conexion.sign_in(mail,pwd)
        print("La respuesta es: " + str(respuesta))
        if respuesta == True:
            return redirect(url_for('home'))    
    return render_template('login.html',form=login_form)



if __name__ == "__main__":
    app.run(port=4005,debug=True)


# Test_Login('usuariodeprueba@gmail.com',"prueba12345")
# Test_Register('prueba_evelyn@gmail.com.ar',"ekisdexD")