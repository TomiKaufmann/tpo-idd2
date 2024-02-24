from flask import Flask, render_template
from views import views
from pymongo import MongoClient
 

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.secret_key = 'your_secret_key'

if __name__ == '__main__':
    app.run(debug=True)
    


 
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
 
# def iniciar_sesion():
#     email = input("Ingrese su email: ")
#     contraseña = input("Ingrese su contraseña: ")
#     usuario = collection_users.find_one({"email": email, "password": contraseña})
#     if usuario:
#         # Crear una nueva sesión para el usuario
#         nueva_sesion = {
#             "email": email,
#             "inicio_sesion": datetime.now(),
#             "actividad": []  # Lista para almacenar la actividad del usuario
#         }
#         collection_sessions.insert_one(nueva_sesion)
#         return print("Inicio de sesión exitoso.")
#     else:
#         return print("El usuario o contraseña no es correcto.")
 
# def recuperar_sesion(username):
#     sesion = collection_sessions.find_one({"username": username})
#     return sesion
 
# def categorizar_usuario():
#     email_usuario = input("Ingrese el email del usuario para saber la categorización: ")
#     sesiones = collection_sessions.find({"email": email_usuario})
   
#     num_total_actividades = 0
#     for sesion in sesiones:
#         num_total_actividades += 1
 
#     print("Número total de actividades:", num_total_actividades)
#     if num_total_actividades >= 10:
#         print("Categoría TOP")
#     elif num_total_actividades >= 5:
#         print("Categoría MEDIUM")
#     else:
#         print("Categoría LOW")
 
# # Llamada a la función
 
# registrar_usuario()
 