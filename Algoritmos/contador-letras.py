# Paso 1: Solicitar entrada al usuario

from operator import length_hint


print('¡Hola usuario1! Bienvenido a mi programa')
palabra = input('Ingrese una palabra: ')
print(palabra)

# Paso 2: Contar la cantidad de letras
cantidad_letras = length_hint(palabra)

# Paso 3: Mostrar al usuario el resultado

print('La palabra ingresada tiene: ', cantidad_letras, 'letras.')