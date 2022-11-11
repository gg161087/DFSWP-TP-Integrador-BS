import json
import hashlib


def HashearPassword(pwd):
    return hashlib.sha256(str(pwd).encode('utf8')).hexdigest()


def ValidarPassword(pwd, pwdHash):    
    return HashearPassword(pwd) == pwdHash


def ValidarUsuario(usuario, pwd):
    with open('app/files/usuarios.json', 'r') as archivo:
        usuarios = json.load(archivo)
        if usuario in usuarios:
            return ValidarPassword(pwd, usuarios[usuario])
        else:
            return False


def CargarPersonas():
    with open('app/files/personas.json', 'r') as archivo:
        personas = json.load(archivo)
    return personas


def SeleccionarPersona(id):
    with open('app/files/personas.json', 'r') as archivo:
        personas = json.load(archivo) 
    for persona in personas:
        if persona['id'] == id:
            return persona
    return None


def RegistrarPersona(datos):
    with open('app/files/personas.json', 'r') as archivo:
        personas = json.load(archivo)    
    if not personas:
        idNuevo = 1
    else:
        idNuevo = int(max(personas, key=lambda x:x['id'])['id']) + 1
    datos['id'] = idNuevo
    personas.append(datos)
    with open('app/files/personas.json', 'w') as archivo:
        json.dump(personas, archivo, indent=6)


def EliminarPersona(id):
    id = int(id)
    with open('app/files/personas.json', 'r') as archivo:
        personas = json.load(archivo)    
    personas = [p for p in personas if p['id'] != id]
    with open('app/files/personas.json', 'w') as archivo:
        json.dump(personas, archivo, indent=6)