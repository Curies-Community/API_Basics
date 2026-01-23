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
#Regresar todas las actividades o una actividad dado un id
@app.get("/actividades")
def leerActividades():
    
    if request.args.get("id") == None:
        return jsonify({
            "actividades": actividades
        }), 200
    
    # Asegurarnos que el id es numerico "1212", "hola"
    # TODO: Hacer una validacion al tipo de dato del id
    idPorEncontrar = int(request.args.get("id"))
    
     #Buscar la actividad
    encontreElId = False
    indiceDeActividades = 0

    #Buscar el id en actividades
    for actividad in actividades:
        if actividad["id"] == idPorEncontrar:
            encontreElId = True
            break
        indiceDeActividades += 1

    if encontreElId == True:
        return jsonify({
            "respuesta": "id encontrado",
            "actividad": actividades[indiceDeActividades]
        }), 200 
    
    return jsonify({
                "respuesta": "id no encontrado"
            }), 400
    


#Este enpoint solo va a aceptar una peticion POST
#El body tiene que ser un json con un titulo y una descripcion

#Crear una actividad 
@app.post("/actividades")
def crearActividad():

    global idUnico
    #repuesta: Request = request
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
        "id": idUnico # ¿Creen que esto funcione?
    })

    idUnicoParaRespuesta = idUnico
    idUnico += 1

    return jsonify({
            "respuesta": "Elemento creado",
            "id": idUnicoParaRespuesta # ¿Creen que esto funcione?
        }), 201

#Endpoint para DELETE
#Borrar todas las actividades o una sola dado un ID
#Borrar todas las actividades de una categoria
@app.delete("/actividades")
def borrarActividades():

    #Si el cliente me pasa el id, es borrar solo ese elemento si existe
    idPorBorrar = int(request.args.get("id"))

    #Si no me pasa el id, borrar todos los elementos
    if idPorBorrar == None:
        actividades.clear()
        return jsonify({
            "respuesta": "Elementos eliminados"
        }), 200
    
    #Buscar la actividad
    encontreElId = False
    indiceDeActividades = 0

    #Buscar el id en actividades
    for actividad in actividades:
        if actividad["id"] == idPorBorrar:
            encontreElId = True
            break
        indiceDeActividades += 1

    if encontreElId == True:
        actividades.pop(indiceDeActividades)
        return jsonify({
            "respuesta": "id borrado con exito"
        }), 200 
    
    return jsonify({
                "respuesta": "id no encontrado"
            }), 400

#Endpoint para PATCH
#Actualizar una actividad
#url/actividades?id=
@app.patch("/actividades")
def actualizarActividad():

    json_repuesta = request.json
    idPorActualizar = int(request.args.get("id"))

    if idPorActualizar == None:
        return jsonify({
            "respuesta": "No me estas pasando el id"
        }), 400

    # Requisito es que nos manden todos el json que quiera actualizar
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
    
    encontreElId = False
    indiceDeActividades = 0
    '''
    actividades = [
        id:0, pos:0
        # id:1, pos:1 - eliminada
        id:2, pos:1
        #id:3, pos:2 - eliminada
        id:4, pos:2
        id:5, pos:3
    ]
    '''

    #Buscar el id en actividades
    for actividad in actividades:
        # ¿Que me hace falta? - ID actividad

        print(type(actividad["id"]), type(idPorActualizar))

        if actividad["id"] == idPorActualizar:
            encontreElId = True
            break
        indiceDeActividades += 1

    if encontreElId == True:
        actividad = actividades[indiceDeActividades]
        actividad["titulo"] = titulo
        actividad["descripcion"] = descripcion
        return jsonify({
                "respuesta": "Actividad actualizada"
            }), 200
    
    return jsonify({
                "respuesta": "id no encontrado"
            }), 400

idUnico = 0
app.run(debug=True)

#PROYECTO

# Sin iniciar - 1
# En Proceso  - 2 
# Terminada   - 3

#POST - Ingresar una categoria
# 1. Sea una categoria valida
# 2. Se agregue la categoria a la actividad
[
    {
        "titulo": "",
        "descripcion": "",
        "categoria": 1
    },
    {
        "titulo": "",
        "descripcion": "",
        "categoria": 3
    },
    {
        "titulo": "",
        "descripcion": "",
        "categoria": 1
    }
]



#GET - Regresar todas las actividades del tipo x (1, 2, 3)
# GET URL/actividades?categoria=1 -> arreglo de todas las actividades de categoria x
# Regresar solamente las atividades del tipo x
# Validar que la categoria sea correcta y en caso de no venga la categoria regresar todos los elementos
'''
actividadesTemp = []
for actividad in actividades:
    if concide:
        actividadesTemp.append()

    return actividadesTemp
'''

#OPCIONAL: id, categoriaURL/actividades?categoria=1&id=2
#OPCIONAL: Validar si es un numero o una string la categoria
'''
[
    {
        "titulo": "",
        "descripcion": "",
        "categoria": 1
    },
    {
        "titulo": "",
        "descripcion": "",
        "categoria": 1
    }
]
'''
# 4 - Regresar un error que diga - 400
'''
{
    "titulo" : "",
    "descripcion" : "",
    ""
}
'''

#PATCH dado un id cambien la categoria
# PATCH URL/actividades?id=1
# Si existe un body con la categoria, actualizar el elemento con id=id
# con la nueva categoria
# Validar que el id exista, validar la categoria y validar que tipo de cambio

# Ejemplo 1 - Sobre escribe la actividad
{
    "titulo": "nueva actividad",
    "descripcion": "nuevo",
    "categoria": 2
}
# Ejemplo 2 - Actualiza la actividad
{
    "categoria": 1
}

#INVALIDO
{
    "titulo": "nuevo",
    "categoria": 1
}
#INVALIDO
{
    "descripcion": "nuevo",
    "categoria": 1
}


#DELETE
#Eliminar todos los elementos que tengan cierta categoria
#DELETE URL/actividades?categoria=1 - NUEVO ENDPOINT
#DELETE URL/actividades?id=2
[
    {
        "titulo": "",
        "descripcion": "",
        "categoria": 1
    },
    {
        "titulo": "",
        "descripcion": "",
        "categoria": 3
    },
    {
        "titulo": "",
        "descripcion": "",
        "categoria": 1
    }
]

'''
actividades = [] 
nuevasActividades = []

for actividad in actividades:
    if actividad.categoria != categoriaABuscar:
        nuevasActividades.append(activida)

actividades = nuevasActividades
return actividades
'''

#Salida con un GET
[
    {
        "titulo": "",
        "descripcion": "",
        "categoria": 3
    }
]
