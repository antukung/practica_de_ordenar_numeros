"""Hola amigos albordeanos aca esta el ultimo y final ejercicio del bingo
tira numeros aleatorios a su manera no se si funciona o no no lo debague correctaamente"""
import random

numeros_eleguidos=[]

print ("Eligamos 4 cartones")
print ("Primer carton")

dar_un_numero= int(input("dame un numero"))
dar_un_numero2=int(input("dame el segundo numero"))
dar_un_numero3=int(input("dame el tercer numero"))
dar_un_numero4=int(input("dame el cuarto numero"))

print ("Segundo carton")

dar_un_numero_segunda_vuelta= int(input("dame un numero"))
dar_un_numero2_segunda_vuelta=int(input("dame el segundo numero"))
dar_un_numero3_segunda_vuelta=int(input("dame el tercer numero"))
dar_un_numero4_segunda_vuelta=int(input("dame el cuarto numero"))

print ("Tercer carton")

dar_un_numero_tercero_vuelta= int(input("dame un numero"))
dar_un_numero2_tercero_vuelta=int(input("dame el segundo numero"))
dar_un_numero3_tercero_vuelta=int(input("dame el tercer numero"))
dar_un_numero4_tercero_vuelta=int(input("dame el cuarto numero"))

print ("Cuarto carton")

dar_un_numero_cuarto_vuelta= int(input("dame un numero"))
dar_un_numero2_cuarto_vuelta=int(input("dame el segundo numero"))
dar_un_numero3_cuarto_vuelta=int(input("dame el tercer numero"))
dar_un_numero4_cuarto_vuelta=int(input("dame el cuarto numero"))

num_ganador = random.randint(1, 10)
num_ganador2 = random.randint(1, 10)
num_ganador3 = random.randint(1, 10)
num_ganador4 = random.randint(1, 10)
num_ganador5 = random.randint(1, 10)
num_ganador6 = random.randint(1, 10)
num_ganador7 = random.randint(1, 10)
num_ganador8 = random.randint(1, 10)
num_ganador9 = random.randint(1, 10)
num_ganador10 = random.randint(1, 10)

numeros_eleguidos.append(num_ganador)
numeros_eleguidos.append(num_ganador2)
numeros_eleguidos.append(num_ganador3)
numeros_eleguidos.append(num_ganador4)
numeros_eleguidos.append(num_ganador5)
numeros_eleguidos.append(num_ganador6)
numeros_eleguidos.append(num_ganador7)
numeros_eleguidos.append(num_ganador8)
numeros_eleguidos.append(num_ganador9)
numeros_eleguidos.append(num_ganador10)

hay_ganador= False
hay_ganador_2=False
hay_ganador_3=False
hay_ganador_4=False


for i in numeros_eleguidos:
    
    if dar_un_numero in numeros_eleguidos and dar_un_numero2 in numeros_eleguidos and dar_un_numero3 in numeros_eleguidos and dar_un_numero4 in numeros_eleguidos:
        hay_ganador= True
        break
    if dar_un_numero_segunda_vuelta in numeros_eleguidos and dar_un_numero2_segunda_vuelta in numeros_eleguidos and dar_un_numero3_segunda_vuelta in numeros_eleguidos and dar_un_numero4_segunda_vuelta in numeros_eleguidos:
        hay_ganador_2= True
        break
    if dar_un_numero_tercero_vuelta in numeros_eleguidos and dar_un_numero2_tercero_vuelta in numeros_eleguidos and dar_un_numero3_tercero_vuelta in numeros_eleguidos and dar_un_numero4_tercero_vuelta in numeros_eleguidos:
        hay_ganador_3= True
        break
    if dar_un_numero_cuarto_vuelta in numeros_eleguidos and dar_un_numero2_cuarto_vuelta in numeros_eleguidos and dar_un_numero3_cuarto_vuelta in numeros_eleguidos and dar_un_numero4_cuarto_vuelta in numeros_eleguidos:
        hay_ganador_4= True
        break
if hay_ganador:
    print ("HAY UN NUMERO GANADOR Y ES EN EL PRIMER CARTON")
elif hay_ganador_2 :
    print ("HAY UN GANADOR Y ES EN EL SEGUNDO CARTON")
elif hay_ganador_3 :
    print ("HAY UN GANADOR Y ES EN EL TERCER CARTON")
elif hay_ganador_4 :
    print ("HAY UN GANADOR Y ES EN EL CUARTO CARTON")
else:
    print ("SON TODOS PERDEDORES")
