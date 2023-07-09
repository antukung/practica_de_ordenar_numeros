""" numeros_ordenados = []

# Ingresar los 10 números
numero1 = int(input("Dame un número: "))
numero2 = int(input("Dame un número: "))
numero3 = int(input("Dame un número: "))
numero4 = int(input("Dame un número: "))
numero5 = int(input("Dame un número: "))
numero6 = int(input("Dame un número: "))
numero7 = int(input("Dame un número: "))
numero8 = int(input("Dame un número: "))
numero9 = int(input("Dame un número: "))
numero10 = int(input("Dame un número: "))

# Agregar los números a una lista
numeros = [numero1, numero2, numero3, numero4, numero5, numero6, numero7, numero8, numero9, numero10]

while numeros:
    # Seleccionar el número mínimo de la lista
    minimo = min(numeros)
    
    # Agregar el número mínimo a la lista ordenada
    numeros_ordenados.append(minimo)
    
    # Eliminar el número mínimo de la lista original
    numeros.remove(minimo)

print("Números ordenados:", numeros_ordenados) """
nombres_y_numeros = []

# Ingresar los 10 números y nombres
for i in range(1, 11):
    numero = int(input(f"Dame el número {i}: "))
    nombre = input(f"Dame el nombre {i}: ")
    nombres_y_numeros.append((numero, nombre))

numeros_ordenados = []

while nombres_y_numeros:
    # Seleccionar el número mínimo de la lista
    minimo = min(nombres_y_numeros, key=lambda x: x[0])
    
    # Agregar el número mínimo a la lista ordenada
    numeros_ordenados.append(minimo)
    
    # Obtener el nombre asociado al número mínimo
    nombre_minimo = minimo[1]
    
    # Eliminar el número mínimo de la lista original
    nombres_y_numeros.remove(minimo)
    
    print(f"Número mínimo: {minimo[0]}, Nombre asociado: {nombre_minimo}")

print("Números ordenados:", numeros_ordenados)