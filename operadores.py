#--------------------------
#OPERADORES ARITMERICOS
#--------------------------
# + , - , * , /
#// para dividir entero, division base (floor division)
# % resto o modulo (modulus)
# ** exponenciacion

a=8
b=4
c=a+b
print(c)

#si no quiero trabajar con flotantes '//'

e = a // b
d = a%b
print(e)
print(d)
#--------------------------
#OPERADORES DE ASIGNACION
#--------------------------
A= 'Este es un texto'
B=234

X = 10

X1 = 15

print(X)

X += X1 #25
X += X1 #40
X += X1 #55
X += X1 #70
X += X1 #85

print(X)

#lo mismo con el '-=' '*=' '/=' '//=' '**='

#--------------------------
#OPERADORES DE COMPARACION
#--------------------------

#No es lo mismo usar el igual para asignar que dos =

x1=5
y1=6

print(x1==y1)

# es distinto? '!='

print(x1 != y1)

# <, >, <=, >=

#--------------------------
#OPERADORES LOGICOS
#--------------------------

#AND Nos va a devolver Verdadero si y solo si ambas afirmaciones son V
#OR Nos va a devolver Verdadero si alguna de las dos afirmaciones es V
#NOT Nos devolvera el lo opuesto al valor que siga

x2= 15

booleano = x2>3 or x2<10
print(booleano)

#es distinto a...
bool = not x2== 18
print(bool)

#--------------------------
#OPERADORES DE IDENTIDAD
#--------------------------

# IS
# IS NOT

#--------------------------
#OPERADORES DE PERTENENCIA
#--------------------------

# IN
# NOT IN

Texto = 'En este texto pondremos algunas tecnologias: Python, R, Django, TensoRFlow'
textominuscula= Texto.lower()
aBuscar = 'TENsORFLOw  '.strip().lower()

print(aBuscar in textominuscula)