# Texto (str)
var1 = 'Texto'
var2 = '1234'
var3 = 'Texto123'

# Numericas (int, float, complex)

var4 = 10
var5 = 2.5
var6 = 1j

print(type(var1))#<class 'str'>
print(type(var2))#<class 'str'>
#si quiero castear deberia cambiar el type por int
print(type(var3))#<class 'str'>
print(type(var4))#<class 'int'>
print(type(var5))#<class 'float'>
print(type(var6))#<class 'complex'>

# ¿Como se castea? (Cambiar de tipo de dato) TipoDeDato ('El dato original')
tupla = ('manzana', 'pera', 'naranja')
list = list(tupla)

print (type(list))
