from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PATCH', 'DELETE'])
def hello():
    if request.method == 'GET':
        return "GET"
    elif request.method == 'POST':
        return "POST"
    else: 
        return f"Hola, eres una peticion de tipo {request.method}"

usuarios = []

#Obtener informacion - Read
@app.get("/usuario")
def obtenerUsuarios():
    #Ejercicio 1: Validar si usuarios puede ser null/None
    return jsonify({
        "usuarios": usuarios
    })

#Crear, postear informacion - Create
@app.post("/usuario")
def agregarUsuario():
    #Leer los datos que me mandan en los parametros de la peticion
    #print(request.args)
    #print(request.args.get("usuario"))
    usuario = request.args.get("usuario")

    if usuario == None:
        return jsonify({
            "respuesta": "No ingresaste el usuario"
        }), 400

    usuarios.append(usuario)
    print(usuarios)
    return jsonify({
        "respuesta": "Se agrego el usuario"
    }), 201

#Actualizar informacion - Update
@app.patch("/usuario")
def actualizarUsuario():
    id = request.args.get("id")
    usuario = request.args.get("usuario")
    if id == None or usuario == None:
        return jsonify({
            "respuesta": "No ingresaste el id o el usuario"
        }), 400
    
    intId = int(id) 
    # Ejercicio 2: try-catch en caso de que el id no se pueda convertir en numero y 
    # regresar un 400 con el error
    if intId < 0 or intId >= len(usuarios):
        return jsonify({
            "respuesta": "El id es invalido"
        }), 400
    
    usuarios[intId] = usuario

    return jsonify({
        "respuesta": "Usuario actualizado"
    }), 201

#Eliminar informacion - Delete
@app.delete("/usuario")
def borrarUsuario():

    usuarios.clear()
    
    #Ejercicio 3: Eliminar un solo usuario

    return jsonify({
        "respuesta": "Todos los usarios eliminados"
    })

app.run(debug=True)