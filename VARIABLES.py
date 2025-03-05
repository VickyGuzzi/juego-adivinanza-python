print('hola mundo')

y=str(x) #casteo de variables

# - str (cadena de caracteres)
texto = 'cadena de caracteres'

#------------------------------
#NUMERICOS
#------------------------------

#- int (entero)
numero_entero = 10

# - float (flotante)
numero_flotante = 3.15

# - complex (complejo)
numero_complejo = 2 + 3j

#-------------------------------
#SECUENCIA
#-------------------------------

# - List (lista [Ordenada y mutable])
lista = [1,2,3,4]

# - tuple (tupla) [colección ordenada e inmutable]

tupla = (1,2,3)

# - range (rango) [secuencia inmutable de numeros]

rango = range(0,10)

#-------------------------------
#MAPPING TYPE (MAPED)
#-------------------------------

#dict (diccionario) [colección no ordenada de pares clave-valor]

diccionario = {
    'nombre': 'Sergio',
    'dirección': 'Av Siemple Viva 300',
    'edad' : 32
    }

#-------------------------------
#SET TYPE (CONJUNTO)
#-------------------------------

# - set (conjunto) [Colección no ordenada y mutable de elementos ÚNICOS (no permite repetir)]

conjunto = {1,2,3,4}

# - frozenset (conjunto inmutable [Conjunto inmutable])

conjunto_inmutable = frozenset({1,2,3,4})

#-------------------------------
#BOOLEAN TYPES (BOOLEANO)
#-------------------------------

# - boolean [puede ser V o F]

booleano = True
booleano2 = False

#-------------------------------
#BINARY TYPES (BINARIO)
#-------------------------------

# - bytes [una secuencia inmutable de bytes]
bytes_data = b'datos'

# - bytearray (array de bytes) [Una secuencia mutable de bytes]
bytearray_data = bytearray(b'datos')

# - memoryview (vista de memoria) [Permite acceder a la memoria de objetos de bytes sin hacer una copia]
memoria = memoryview(b'datos')

#-------------------------------
#NONE/NULO (NULO)
#-------------------------------

#NoneType (nulo) [Representa la ausencia de valor o la no definición]
nulo=None

string_comillas_simples = 'Hola, mundo!'
string_comillas_dobles = "Hola, mundo!"
string_comillas_triples = '''Este texto pueede ser
multilena'''
string_comillas_triples2 = """Este texto tambien
puede ser multiples lineas"""

