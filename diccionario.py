provincias_capitales = {}

while True:
    provincia = input("Ingrese el nombre de la provincia (o 0 para salir): ")
    
    if provincia == '0':
        break
    
    capital = input("Ingrese el nombre de la capital: ")
    provincias_capitales[provincia] = capital
while True:
    consulta = input("Ingrese el nombre de la provincia a consultar (o 0 para salir): ")
    
    if consulta == '0':
        break
    
    if consulta in provincias_capitales:
        capital = provincias_capitales[consulta]
        print(f"La capital de {consulta} es {capital}")
    else:
        print("Provincia no encontrada")
    
while True:
    reconsulta= input ("Consulte el nombre de todas la provincias y capitales inscriptas en el programa tipendo todas o 0 para salir: ")

    if reconsulta == '0':
        break
    if reconsulta == 'todas':
        print("Diccionario de provincias y capitales:")
        for provincia, capital in provincias_capitales.items():
            print(f"{provincia}: {capital}")