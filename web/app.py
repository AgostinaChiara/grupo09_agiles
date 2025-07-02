from flask import Flask, render_template, request, jsonify, session
import sys
import os
import uuid
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ahorcado import Ahorcado

app = Flask(__name__)
app.secret_key = os.urandom(24) 

# Mapeo de dificultad a número
dificultades = {
    "facil": 1,
    "medio": 2,
    "dificil": 3
}

juegos_activos = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/juego")
def juego():
    return render_template("juego.html")

@app.route('/juego/nuevo', methods=['POST'])
def juego_nuevo():
    dificultad = request.json.get("dificultad", "medio").lower()
    dificultad_num = dificultades.get(dificultad, 2)
    juego = Ahorcado(dificultad=dificultad_num)
    
    session['juego'] = juego.__dict__  # Guardamos estado como dict
    id_juego = str(uuid.uuid4())

    juegos_activos[id_juego] = juego

    return jsonify({
        "idJuego": id_juego,
        "palabraActual": juego.palabra_actual(),
        "intentosRestantes": juego.intentos_restantes,
        "errores": juego.intentos_maximos - juego.intentos_restantes,
        "terminado": juego.juego_terminado,
        "victoria": juego.victoria
    })

@app.route('/juego/letra', methods=['POST'])
def arriesgar_letra():
    letra = request.json.get("letra", "").lower()
    id_juego = request.json.get("idJuego")

    juego = juegos_activos.get(id_juego)

    juego.arriesgar_letra(letra)
    
    session['juego'] = juego.__dict__

    palabra_secreta = juego.palabra_secreta if juego.juego_terminado else "XXXXXXXX"
    return jsonify({
        "palabraActual": juego.palabra_actual(),
        "intentosRestantes": juego.intentos_restantes,
        "errores": juego.intentos_maximos - juego.intentos_restantes,
        "terminado": juego.juego_terminado,
        "victoria": juego.victoria,
        "letraCorrecta": letra in juego.palabra_secreta,
        "secreta": palabra_secreta,
        "sesion": session['juego']
    })

if __name__ == "__main__":
    app.run(debug=True)