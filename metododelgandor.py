"""
numeros_ordenados = []

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

# Grupo 1: Competencia entre los números 1 al 10
ganador_grupo_final = min(numero1, numero2, numero3, numero4, numero5,numero6, numero7,numero8, numero9, numero10)

# Seleciona del menor
numeros_ordenados.extend([ganador_grupo_final])

print("Números ordenados:", numeros_ordenados)

"""
numeros_ordenados = []

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

print("Números ordenados:", numeros_ordenados)

