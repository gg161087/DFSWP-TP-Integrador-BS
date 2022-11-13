from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    pwd = PasswordField('Contraseña', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Iniciar sesión')


class RegisterPersonForm(FlaskForm):
    fecha = DateField('Fecha', format='%Y-%m-%d')
    nombre = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    apellido = StringField('Apellido', validators=[DataRequired('Este campo es requerido')])
    dni = StringField('D.N.I', validators=[DataRequired('Este campo es requerido')])
    motivo = StringField('Motivo', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Agregar nueva persona')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-secondary', 'formnovalidate': 'True'})

class EditPersonForm(FlaskForm):    
    fecha = DateField('Fecha', format='%Y-%m-%d')
    nombre = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    apellido = StringField('Apellido', validators=[DataRequired('Este campo es requerido')])
    dni = StringField('D.N.I', validators=[DataRequired('Este campo es requerido')])
    motivo = StringField('Motivo', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Guardar')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-secondary', 'formnovalidate': 'True'})