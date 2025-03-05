#Slicing ponemos desde un indice hasta un indice NO incluido
txt = "Seguimos trabajando con Strings"
print(txt [8:19])

#Si quiero desde el comienzo hasta un numero
print(txt[:8])
print(txt[-7:])

#Desde un string hasta el final
print(txt[23:])

txt2= 'CUANDO ESCRIBO EN MAYUSCULAS LA GENTE PIENSA QUE ESTOY GRITANDO'
print(txt2.lower())

txt3 = 'este texto'
mayuscula = txt.upper()
print(mayuscula)

txt4= '         Uy! me deje unos espacios     '
txtcorregido= txt4.strip()
print(txtcorregido)