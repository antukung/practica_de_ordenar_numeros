"""Hola Albordeanos en mi intento de seguir practicando
CODIGO logre hacer que dos numero se ordenen hay que ver
si consigo efectivizarlo para 4 numeros lo que seria un
golazo SALUDOS DESDE EL PATO BERAZATHEGUI. Son 16 lineas
de codigo del amor"""

print ("dame dos numeros")

numero1= input()
numero2= input ()

arreglo_numeros=[]

if (numero1>numero2):
    arreglo_numeros.append(numero2)
    arreglo_numeros.append(numero1)
else:
    arreglo_numeros.append(numero1)
    arreglo_numeros.append(numero2)

print ("Estos son tus dos numeros:")
print (arreglo_numeros)
