#Estructuras de control condicionales
#-------------------------------------
#if,elif,else
#-------------------------------------

x=9
if x>0:
    print('X es un número positivo')
elif x<0:
    print('X es un número negativo')
else:
    print('X es igual a 0')

# Qusieramos viajar internacionalmente

visa = True
pasaporte = True

if visa and pasaporte:
    print('Puedes ingresar al país de destino')
elif pasaporte and not visa:
    print('Puedes ingresar sólo a paises que no requieren Visa')
else:
    print('Debes conseguir la documentación antes de viajar')

# Quisieramos sacar la licencia de conducir

edad = 22

if edad > 21:
    print('Puede sacar la licencia de conducir')
elif edad < 21:
    print('No puede sacar la licencia de conducir')

edadnueva = 15

if edadnueva < 18 or edadnueva > 60:
    if edadnueva < 18:
        print('No tienes edad suficiente para entrar a la disco')
    else:
            print('Por una cuestion de seguridad no se permite ingreso a mayores de 60 años')
elif edadnueva >= 18 and edadnueva <= 60:
    ('Puedes ingresar a la disco')


#-------------------------------------
#While ßucles (mientras se cumpla una condicion)
#-------------------------------------

Contador = 0
Limite = 5
Sumatoria = 0

while Contador <= Limite:
    Sumatoria += Contador
    Contador += 1
print('La suma de los numeros hasta:', Limite, 'es', Sumatoria)

#-------------------------------------
#FOR
#-------------------------------------

for i in range(5):
    print(i)

for e in range(1,11,2):
    print(e)

for u in range(100):
    if u == 50 :
        print('Paso por el numero 50')


#-------------------------------------
#try, except, finally: manejo de errores
#-------------------------------------

#Manejo de la division por cero
a=10
b=0

try:
    resultado = a/b
    print(resultado)
except ZeroDivisionError:
    print('No se puede dividir por cero')
finally:
    resultado=0
print('Hola mi nombre es Vicky y este mensaje quiero que salga a pesar de los errores')

#-------------------------------------
#Break continue pass
#-------------------------------------

#hace que no se siga ejecutando lo q esta dentro del bucle

contador = 10
prohibido = 23

while contador <25:
    print(contador)
    if contador == prohibido:
        break
    contador += 1
print(contador)

#bucle infinito si pongo continue

cont= 0
while cont <5:
    print(cont)
    cont += 1
    if cont == 3:
        continue
    
print(cont)

#pass

age=19

if age > 18:
    print('Puedes ingresar a esta institucion')
elif age == 18:
    pass
else:
    print('No tienes edad suficiente para entrar aqui')
