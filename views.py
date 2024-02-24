from flask import Blueprint, render_template, redirect, url_for, request, session
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, DuplicateKeyError, WriteError
from datetime import datetime
from urllib.parse import quote_plus
import bcrypt

views = Blueprint(__name__,"/login")

#Database

def connect_db(user_mail = 'kikiazcoaga',user_password = 'uade123'):
    try:
        escaped_username = quote_plus(user_mail)
        escaped_password = quote_plus(user_password)
        # Intentamos establecer la conexión con MongoDB Atlas
        mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@projectbd2.jcixys6.mongodb.net/?retryWrites=true&w=majority&appName=ProjectBD2"
        client = MongoClient('mongodb+srv://kikiazcoaga:uade123@projectbd2.jcixys6.mongodb.net/''?retryWrites=true&w=majority&appName=ProjectBD2')
    
        # Seleccionamos la base de datos y la colección
        db = client['ProjectDB2']
        collection_users = db['Users']
        collection_sessions = db['Sessions']
    except ConnectionFailure as e:
        print(f"Error de conexión a MongoDB Atlas: {e}")
    return db

def add_new_user(new_user_mail,new_user_password):
    escaped_username = quote_plus('kikiazcoaga')
    escaped_password = quote_plus('uade123')
    mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@projectbd2.jcixys6.mongodb.net/?retryWrites=true&w=majority&appName=ProjectBD2"
    client = MongoClient('mongodb+srv://kikiazcoaga:uade123@projectbd2.jcixys6.mongodb.net/''?retryWrites=true&w=majority&appName=ProjectBD2')
    db = client['ProjectDB2']
    #Verificar nombre de user existente
    if db['Users'].find_one({'email': new_user_mail}):
        error = 'Ese mail ya está registrado'
        return render_template('register.html', error=error)
    
    # hashed_pw = bcrypt.hashpw(new_user_password.encode('utf-8'), bcrypt.gensalt())
    
    db['Users'].insert_one({'email': new_user_mail, 'password': new_user_password})




@views.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Access the form data using request.form
        user_mail = request.form['user_mail']
        user_password = request.form['user_password']
        db = connect_db(user_mail,user_password)
        user_data = db['Users'].find_one({'email': user_mail})
        
        if user_data:
            session['user_id'] = str(user_data['_id'])
            return redirect(url_for('views.home', user_mail=user_mail, user_password = user_password))
        else:
            error = 'pifiaste'
            return render_template('login.html', error = error )
        
    return render_template('login.html')

@views.route("/register", methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        new_user_mail = request.form['user_mail']
        new_user_password = request.form['user_password']    
        add_new_user(new_user_mail,new_user_password)
        return render_template("/home", user_mail = new_user_mail)

    return render_template('register.html')

@views.route("/home")
def home():
    if 'user_id' in session:
        db = connect_db()
        user_data = db['Users'].find_one({'_id': ObjectId(session['user_id'])})
        return render_template('home.html',user_mail=user_data['email'])
    else:
        return redirect(url_for('login'))

#Functions

# def registrar_usuario():
#     try:
#         email = input("Ingrese un nuevo email: ")
#         password = input("Ingrese una nueva contraseña: ")
#         # Datos del nuevo usuario a insertar
#         nuevo_usuario = {
#             "email": email,
#             "password": password,
#         }
#         # Insertar el nuevo usuario en la colección
#         collection_users.insert_one(nuevo_usuario)
#         print("Usuario registrado exitosamente.")
 
#     except DuplicateKeyError:
#         print("Error: El nombre de usuario o correo electrónico ya existe en la base de datos.")
       
#     except WriteError as e:
#         print(f"Error al escribir en la base de datos: {e}")