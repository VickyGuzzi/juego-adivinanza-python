import random
numero_secreto = random.randint(0,100)
adivinado = False

print('¡Bienvenido al juego de adivinar el número secreto! ')

while not adivinado:
    entrada = input('Introduce un número del 1 al 99: ') # To do convertir a numero
    numero = int(entrada)

    if numero == numero_secreto:
        print('¡Felicitaciones has adivinado el número secreto!')
        adivinado = True
    elif numero < numero_secreto:
        print('El número es mayor al ingresado')
    else:
        print('El número es menor al ingresado')
