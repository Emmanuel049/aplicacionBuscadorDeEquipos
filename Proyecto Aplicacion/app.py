#---------------------------------- FLASK --------------------------------------

from flask import Flask, render_template
from flask import request
import forms
from cmath import log
from distutils.log import Log
import Prueba_conexion

app = Flask(__name__)
# clase a ejecutar para obtener la coneccion, con parametro __name__

@app.route("/", methods = ['GET','POST'])
def Index():
    comment_form = forms.CommentForm(request.form)



    if request.method == 'POST' and comment_form.validate():
        mail = comment_form.username.data
        pwd = comment_form.password.data
        print(mail,pwd)
        respuesta = Prueba_conexion.sign_in(mail,pwd)
        # comment_form['repuesta'] = respuesta
        print("La respuesta es: " + str(respuesta))
    return render_template('index.html',form=comment_form)

if __name__ == "__main__":
    app.run(port=4005,debug=True)


# Test_Login('usuariodeprueba@gmail.com',"prueba12345")
# Test_Register('prueba_evelyn@gmail.com.ar',"ekisdexD")