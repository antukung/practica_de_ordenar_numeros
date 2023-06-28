"""ACA ESTA ALBORDEANOS EL DEL BINGO UNO SIGAN PROGRAMANDO POR FAVOR
JAJAJAJA QUE LINDO PROGRAMAR"""



numeros_ganadores=[6,21,45,7]

dar_un_numero= int(input("dame un numero"))
dar_un_numero2=int(input("dame el segundo numero"))
dar_un_numero3=int(input("dame el tercer numero"))
dar_un_numero4=int(input("dame el cuarto numero"))

hay_ganador= False

for i in numeros_ganadores:
    
    if i==dar_un_numero or i==dar_un_numero2 or i==dar_un_numero3 or i==dar_un_numero4:
        hay_ganador= True
        break

if hay_ganador:
    print ("HAY UN NUMERO GANADOR")
else:
    print ("SON TODOS PESIMOS NUMEROS")