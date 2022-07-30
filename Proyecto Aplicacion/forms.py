from wtforms import Form, StringField, validators,PasswordField

class CommentForm(Form):
    
    username = StringField('Usuario', [validators.Length(min=4, max=25)])
    password  = PasswordField('Contraseña')