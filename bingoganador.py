"""ACA ESTA ALBORDEANOS EL DEL BINGO UNO SIGAN PROGRAMANDO POR FAVOR
JAJAJAJA QUE LINDO PROGRAMAR"""



numeros_ganadores=[6,21,45,7]

dar_un_numero= input("dame un numero")
dar_un_numero2=input("dame el segundo numero")
dar_un_numero3=input("dame el tercer numero")
dar_un_numero4=input("dame el cuarto numero")

for i in range(len(numeros_ganadores)):
    elnumero=numeros_ganadores=[i]
    if (elnumero==dar_un_numero) or (elnumero==dar_un_numero2) or (elnumero==dar_un_numero3) or (elnumero==dar_un_numero4):
        print ("TIENES AL MENOS UN NUMERO GANDOR")
    else:
        print ("NINGUN NUMERO ES GANADOR")