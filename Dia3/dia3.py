from flask import Flask
from flask import request
from flask import Request
from flask import jsonify

#Crear la primer app en flask
app = Flask(__name__)

#Esto por defecto es una peticion get
@app.route("/")
def holaMundo():
    return "Hola mundo!"

# CRUD - Create, Read, Update, Delete

# Crear, Leer, Actualizar, Borrar

# Metodos HTTP - GET, POST, PATCH, DELETE

# Leer       - Read   - GET
# Crear      - Create - POST
# Actualizar - Update - PATCH
# Borrar     - Delete - DELETE

# Codigos de respuesta
# 200 - 299 -> Todo OK
# 400 - 499 -> El cliente hizo algo mal
# 500 - 599 -> El servidor hizo algo mal

# ToDo App
#   endpoints
#   /.../...
#   Envio/Recibir
#   Seguridad
#   Escalibilidad

# Crear actividades/task - Create - POST
#   Titulo: "Hacer el super"
#   Descripcion: "Leche, huevos, carne, pollo, etc."

# Actualizar las actividades/task - Update - PATCH
#   Titulo: "Hacer el super" -> "Hacer el super en la mañana"
#   Descripcion: "Leche, huevos, carne, pollo, etc." 
#       -> "Leche, huevos, carne, pollo, cafe, etc"

# Borrar actividades/task - Delete - Delete
#  Dado algo (id, titulo, descripcion) borrar la actividad/task

# Leer actividades/task - Read - GET 
#   Leer todas mis actividades

#Ejemplo con methods
'''
@app.route("/api", methods=["GET", "POST"])
def crearActividad():
    if request.method == "GET":
        return "Soy un GET"
    elif request.method == "POST":
        return "Soy un POST"
    else:
        return "Metodo no encontrado"
'''
#Dentro vamos a guardar un json
'''
{
    "titulo" : "",
    "descripcion" : ""
}
'''

actividades = []

#Este endpoint solo va a aceptar una peticion GET
@app.get("/actividades")
def leerActividades():
    return jsonify({
        "actividades": actividades
    }), 200

#Este enpoint solo va a aceptar una peticion POST
#El body tiene que ser un json con un titulo y una descripcion
'''
{
    "titulo" : "",
    "descripcion" : ""
}
'''
@app.post("/actividades")
def crearActividad():
    repuesta: Request = request
    json_repuesta = request.json

    #Validar siempre los datos
    if 'titulo' not in json_repuesta or 'descripcion' not in json_repuesta:
        return jsonify({
            "respuesta": "titulo o descripcion no encontrados"
        }), 400

    titulo = json_repuesta["titulo"]
    descripcion = json_repuesta["descripcion"]
    
    if titulo == None or descripcion == None or titulo == "" or descripcion == "":
        return jsonify({
            "respuesta": "titulo o descripcion no deben de ser vacios"
        }), 400
    
    actividades.append({
        "titulo": titulo,
        "descripcion": descripcion,
        "id": len(actividades) # ¿Creen que esto funcione?
    })

    return jsonify({
            "respuesta": "Elemento creado",
            "id": len(actividades) # ¿Creen que esto funcione?
        }), 201

@app.delete("/actividades")
def borrarActividades():

    actividades.clear()

    return jsonify({
        "respuesta": "Elementos eliminados"
    })

#id - 
@app.patch("/actividades")
def actualizarActividad():
    # Este endpoint es para la siguiente clase,
    # se deja como ejercicio pensar en la implementacion
    return "<HACER LA RESPUESTA>"

app.run(debug=True)