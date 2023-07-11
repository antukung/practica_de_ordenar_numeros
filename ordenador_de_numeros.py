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

# Ingresar las 7 notas de cada materia y nombres
for i in range(1, 11):
    nota1 = int(input(f"Dame la nota de matemacica {i}: "))
    nota2 = int(input(f"Dame la nota de lengua {i}: "))
    nota3 = int(input(f"Dame la nota de ciencias sociales {i}: "))
    nota4 = int(input(f"Dame la nota de ciencias naturales {i}: "))
    nota5 = int(input(f"Dame la nota de arte {i}: "))
    nota6 = int(input(f"Dame la nota de ingles {i}: "))
    nota7 = int(input(f"Dame la nota de educacion fisica {i}: "))
    promedio= (nota1+nota2+nota3+nota4+nota5+nota6+nota7)/7
    nombre = input(f"Dame el nombre {i}: ")
    nombres_y_numeros.append((promedio, nombre))

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