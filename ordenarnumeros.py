"""Hola amigos del CURSO PROGRAMACION ALBORDE ESTO ES U INTENTO 
de pasar el codigo que vimos que ordenaba numeros a PYTHON .Todabia
le falta bastante. No entiendo como hacer para colocar los numeros en
las lista o bien como hacer el ciclo FOREACH, pero va queriendo.
Sigan programando"""



print ("dame cuatro numeros consecutivos!!!")

numero1= input()
numero2= input()
numero3= input()
numero4= input()

lista_numeros=[numero1,numero2,numero3,numero4]
cantidad_de_numeros= len(lista_numeros)
lista_numeros_ordenada=[]
for i in lista_numeros:
    if (cantidad_de_numeros==0):
        lista_numeros_ordenada.append(numero1)
    elif (cantidad_de_numeros >0):
        for i in lista_numeros_ordenada:
            if (lista_numeros[0]<lista_numeros[i]):
                lista_numeros_ordenada.insert(0,numero2)
    else:
        lista_numeros_ordenada.append(numero4)
print ("esta es tu lista")
print (lista_numeros_ordenada)
    
