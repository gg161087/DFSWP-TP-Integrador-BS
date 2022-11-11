from flask import render_template, redirect, url_for, session, flash, request
from app.auth import login_required
from app import app
from app.forms import LoginForm, RegistrarPersonaForm, EditarPersonaForm
from app.handlers import *


@app.route('/')
@app.route('/index')
@login_required
def index():
    if request.method == 'GET' and request.args.get('borrar'):
        EliminarPersona(request.args.get('borrar'))
        flash('Se ha eliminado la persona', 'success')
    return render_template('index.html', titulo="Inicio", personas=CargarPersonas())


@app.route('/registrar_persona', methods=['GET', 'POST'])
@login_required
def registrar_persona():
    personaForm = RegistrarPersonaForm()
    if personaForm.cancelar.data:
        return redirect(url_for('index'))
    if personaForm.validate_on_submit():
        fecha = str(personaForm.fecha.data)
        datos = {
            'fecha': fecha,
            'nombre': personaForm.nombre.data, 
            'apellido': personaForm.apellido.data, 
            'dni': personaForm.dni.data,
            'motivo': personaForm.motivo.data
        }        
        RegistrarPersona(datos)
        flash('Se agregado una nueva persona', 'success')
        return redirect(url_for('index'))
    return render_template('registrar_persona.html', titulo="Persona", personaForm=personaForm)


@app.route('/editar_persona/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_persona(id):
    personaForm = EditarPersonaForm(data=SeleccionarPersona(id))
    if personaForm.cancelar.data:
        return redirect(url_for('index'))
    if personaForm.validate_on_submit():              
        datos = {
            'fecha': personaForm.fecha.data,
            'nombre': personaForm.nombre.data, 
            'apellido': personaForm.apellido.data, 
            'dni': personaForm.dni.data,
            'motivo': personaForm.motivo.data
        }
        EliminarPersona(id)
        RegistrarPersona(datos)
        flash('Se ha editado a la persona exitosamente', 'success')
        return redirect(url_for('index'))
    return render_template('editar_persona.html', titulo="Persona", personaForm=personaForm)


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        usuario = loginForm.usuario.data
        pwd = loginForm.pwd.data
        if ValidarUsuario(usuario, pwd):
            session['usuario'] = usuario
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html', titulo="Login", loginForm=loginForm)


@app.route('/logout')
@login_required
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))