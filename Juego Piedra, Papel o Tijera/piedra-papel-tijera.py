nombre1 = input('¿Cómo se llamará el jugador 1? ')
nombre2 = input('¿Cómo se llamará el jugador 2? ')

puntos_jugador1 = 0
puntos_jugador2 = 0
cant_max_puntos = 2  # Se necesita ganar 2 veces para ser el mejor de 3

while puntos_jugador1 < cant_max_puntos and puntos_jugador2 < cant_max_puntos:
    jugador1 = input(f'¡Hola {nombre1}! ¿Qué eliges? ¿Piedra, papel o tijeras? ').lower()
    jugador2 = input(f'¡Hola {nombre2}! ¿Qué eliges? ¿Piedra, papel o tijeras? ').lower()

    if jugador1 == jugador2:
        print('¡Ha sido un empate!')
    elif (jugador1 == 'piedra' and jugador2 == 'tijeras') or \
         (jugador1 == 'papel' and jugador2 == 'piedra') or \
         (jugador1 == 'tijeras' and jugador2 == 'papel'):
        print(f'¡{nombre1} gana esta ronda!')
        puntos_jugador1 += 1
    else:
        print(f'¡{nombre2} gana esta ronda!')
        puntos_jugador2 += 1

    print(f"Puntaje: {nombre1} {puntos_jugador1} - {nombre2} {puntos_jugador2}")

if puntos_jugador1 > puntos_jugador2:
    print(f'¡{nombre1} ha ganado la partida!')
else:
    print(f'¡{nombre2} ha ganado la partida!')
