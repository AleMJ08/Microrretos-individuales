# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("perfil_2_3_2.html", estudiante="Alejandro Muñoz Jiménez", nickname="AlePY", id_dev="8923")

if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)