"""Hola compas en este ejercicio cambie algunas cosas para crear 
numeros aletorios, esta bueno pruevenlo"""

import random

numeros_eleguidos=[]

dar_un_numero= int(input("dame un numero"))
dar_un_numero2=int(input("dame el segundo numero"))
dar_un_numero3=int(input("dame el tercer numero"))
dar_un_numero4=int(input("dame el cuarto numero"))

num_ganador = random.randint(1, 10)
num_ganador2 = random.randint(1, 10)
num_ganador3 = random.randint(1, 10)
num_ganador4 = random.randint(1, 10)

numeros_eleguidos.append(num_ganador)
numeros_eleguidos.append(num_ganador2)
numeros_eleguidos.append(num_ganador3)
numeros_eleguidos.append(num_ganador4)

for i in numeros_eleguidos:
    
    if i==dar_un_numero or i==dar_un_numero2 or i==dar_un_numero3 or i==dar_un_numero4:
        hay_ganador= True
        break

if hay_ganador:
    print ("HAY UN NUMERO GANADOR")
else:
    print ("SON TODOS PESIMOS NUMEROS")

