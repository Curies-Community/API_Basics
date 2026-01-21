from flask import Flask

#Comando para ejecutar el programa: python dia1.py

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hola mundo!"

app.run(debug=True)