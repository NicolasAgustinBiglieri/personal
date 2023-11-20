
import numpy as np
import time


# Creamos una funcion piedra, papel o tijera

def piedra_papel_tijera():

    # Creamos un diccionario para colocar cual vence a cual
    opciones = {'piedra': 'tijera', 'papel': 'piedra', 'tijera': 'papel'}

    # Entrada del jugador
    jugador = input("Elije piedra, papel o tijera: ")
    while jugador not in {'piedra', 'papel', 'tijera'}:
        print("Ha cometido un error")
        jugador = input("Elije piedra, papel o tijera: ")

    # Seleccion aleatoria para la computadora
    computadora = np.random.choice(['piedra', 'papel', 'tijera'])

    # Mostrar las selecciones
    time.sleep(.5)
    print("\nHas seleccionado:", jugador)
    print("La computadora ha seleccionado", computadora, "\n")
    time.sleep(2)

    # Determinar ganador
    if opciones[jugador] == computadora:
        print("¡Has ganado!")
    if opciones[computadora] == jugador:
        print("¡Has perdido!")
    else:
        print("¡Empate!")
