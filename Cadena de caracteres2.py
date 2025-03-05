a='Hola'
b='Mundo'
c= a + ' ' + b
print(c)

txt= 'El contenido de este curso va a durar: '
horas = 10
concatenado = txt + str(horas) + ' horas'

print(concatenado)

#otra forma
clases = 60
txt2= 'El contenido de este curso va a durar: {} horas y tendrá {} clases'

print(txt.format(clases, horas))

# con la barra \ invertida podremos hacer 'escape de caracteres'

txt3= 'La mejor serie que vi en mi vida es \'GAME OF THRONES\''
print(txt3)

#salto de linea '\n', y este: '\b' elimina el ultimo caracter

txt4= 'La abuela esta en su dpto_\b: '
print(txt4)

