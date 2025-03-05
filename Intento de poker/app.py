from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # Necesario para usar sesiones

# Función para repartir las cartas
def repartir_cartas(num_jugadores):
    palos = ['Corazones', 'Tréboles', 'Diamantes', 'Picas']
    valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    mazo = [f'{valor} de {palo}' for palo in palos for valor in valores]
    random.shuffle(mazo)  # Barajar el mazo
    
    manos = []
    for i in range(num_jugadores):
        mano = mazo[i::num_jugadores]  # Reparte las cartas de manera equitativa
        manos.append(mano)

    return manos

# Inicialización del juego
def iniciar_juego():
    session['turno'] = 0  # El primer jugador es el turno 0
    session['num_jugadores'] = 4
    session['manos'] = repartir_cartas(session['num_jugadores'])
    session['cartas_jugadas'] = []  # Lista para llevar el control de las cartas jugadas

@app.route('/')
def index():
    # Verificar si el juego ya está en curso, sino iniciarlo
    if 'manos' not in session:
        iniciar_juego()

    # Obtener el turno actual
    turno_actual = session['turno']
    manos = session['manos']
    jugador_actual = turno_actual + 1  # Jugador 1, 2, 3, 4
    
    return render_template('index.html', manos=manos, turno_actual=turno_actual, jugador_actual=jugador_actual)

@app.route('/jugada', methods=['POST'])
def jugada():
    carta = request.form.get('carta')  # Obtener la carta seleccionada
    turno_actual = session['turno']
    cartas_jugadas = session['cartas_jugadas']
    
    # Agregar la carta jugada a la lista de cartas jugadas
    cartas_jugadas.append(carta)
    session['cartas_jugadas'] = cartas_jugadas
    
    # Cambiar al siguiente turno
    turno_actual = (turno_actual + 1) % session['num_jugadores']
    session['turno'] = turno_actual
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5002)
