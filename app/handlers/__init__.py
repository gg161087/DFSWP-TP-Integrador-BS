import json
import hashlib


def hashear_password(pwd):
    return hashlib.sha256(str(pwd).encode('utf8')).hexdigest()


def validate_password(pwd, pwdHash):    
    return hashear_password(pwd) == pwdHash


def validate_user(user, pwd):
    with open('app/files/usuarios.json', 'r') as file:
        users = json.load(file)
        if user in users:
            return validate_password(pwd, users[user])
        else:
            return False


def upload_people():
    with open('app/files/personas.json', 'r') as file:
        people = json.load(file)
    return people


def select_person(person_id):
    with open('app/files/personas.json', 'r') as file:
        people = json.load(file) 
    for person in people:
        if person['id'] == person_id:
            return person
    return None


def register_person(data):
    with open('app/files/personas.json', 'r') as file:
        people = json.load(file)    
    if not people:
        new_id = 1
    else:
        new_id = int(max(people, key=lambda x:x['id'])['id']) + 1
    data['id'] = new_id
    people.append(data)
    with open('app/files/personas.json', 'w') as file:
        json.dump(people, file, indent=6)


def delet_person(person_id):
    person_id= int(person_id)
    with open('app/files/personas.json', 'r') as file:
        people = json.load(file)    
    people = [p for p in people if p['id'] != person_id]
    with open('app/files/personas.json', 'w') as file:
        json.dump(people, file, indent=6)