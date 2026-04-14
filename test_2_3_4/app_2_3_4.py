# Importamos la clase Flask desde el paquete instalado
from flask import Flask, render_template

# Creamos una instancia de la aplicación. __name__ ayuda a Flask a localizar archivos
app = Flask(__name__)

@app.route("/coleccion")
def ver_coleccion():
    # Creamos una lista de diccionarios con datos de prueba
    mis_favoritos = [
        {"nombre": "C++", "motivo": "Destaca su velocidad, acceso directo a memoria y la orientación a objetos"},
        {"nombre": "JavaScript", "motivo": "Tiene una ejecución rápida y es versátil tanto para backend como para frontend"},
        {"nombre": "Python", "motivo": "Posee una amplia librería, ideal para la inteligencia artificial y datos"},
    ]
    # Enviamos la lista completa a la plantilla con el nombre 'items'
    return render_template("galeria.html", items=mis_favoritos)

# Comprobamos si el script se está ejecutando directamente (y no importado como módulo)
if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)