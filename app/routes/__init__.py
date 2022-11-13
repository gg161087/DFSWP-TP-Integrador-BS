from flask import render_template, redirect, url_for, session, flash, request
from app.auth import login_required
from app import app
from app.forms import *
from app.handlers import *
from datetime import datetime

@app.route('/')
@app.route('/index')
@login_required
def index():
    if request.method == 'GET' and request.args.get('eliminar'):
        delet_person(request.args.get('eliminar'))
        flash('Se ha eliminado la persona', 'success')
    return render_template('index.html', titulo="Inicio", personas=upload_people())


@app.route('/registrar_persona', methods=['GET', 'POST'])
@login_required
def registrar_persona():
    person_form = RegisterPersonForm()
    if person_form.cancelar.data:
        return redirect(url_for('index'))
    if person_form.validate_on_submit():
        fecha = str(person_form.fecha.data)
        datos = {
            'fecha': fecha,
            'nombre': person_form.nombre.data, 
            'apellido': person_form.apellido.data, 
            'dni': person_form.dni.data,
            'motivo': person_form.motivo.data
        }        
        register_person(datos)
        flash('Se agregado una nueva persona', 'success')
        return redirect(url_for('index'))
    return render_template('registrar_persona.html', titulo="Persona", personaForm=person_form)


@app.route('/editar_persona/<int:id>', methods=['GET'])
@login_required
def get_editar_persona(id):
    person_form = EditPersonForm(data=select_person(id))
    person_form.fecha.data = datetime.strptime(person_form.fecha.data, '%Y-%m-%d') 
    return render_template('editar_persona.html', titulo="Persona", personaForm=person_form)


@app.route('/editar_persona/<int:id>', methods=['POST'])
@login_required
def post_editar_persona(id):
    person_form = EditPersonForm(data={})
    if person_form.cancelar.data:
        return redirect(url_for('index'))
    if person_form.validate_on_submit():     
        fecha = str(person_form.fecha.data)           
        datos = {
            'fecha': fecha,
            'nombre': person_form.nombre.data, 
            'apellido': person_form.apellido.data, 
            'dni': person_form.dni.data,
            'motivo': person_form.motivo.data
        }
        delet_person(id)
        register_person(datos)
        flash('Se ha editado a la persona exitosamente', 'success')
        return redirect(url_for('index'))   


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        usuario = login_form.usuario.data
        pwd = login_form.pwd.data
        if validate_user(usuario, pwd):
            session['usuario'] = usuario
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html', titulo="Login", loginForm=login_form)


@app.route('/logout')
@login_required
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))