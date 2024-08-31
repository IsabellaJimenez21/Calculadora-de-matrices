# Definición de matrices a usar
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Suma de matrices
def sumar_matrices (matriz_a, matriz_b):
    suma_resultado = [] 
    for i in range(len(matriz_a)):  # Recorre las filas de la matriz
        fila = []
        for j in range(len(matriz_a[i])):  # Recorre las columnas de la matriz
            suma = matriz_a[i][j] + matriz_b[i][j]  # Suma los elementos correspondientes
            fila.append(suma)  # Añade el resultado a la fila
        suma_resultado.append(fila) # Añade la fila completa a la matriz de resultado
    return suma_resultado


# Resta de matrices
def restar_matrices (matriz_a, matriz_b):
    resta_resultado = []
    for i in range(len(matriz_a)):  # Recorre las filas de la matriz
        fila = []
        for j in range(len(matriz_a[i])):  # Recorre las columnas de la matriz
            resta = matriz_a[i][j] - matriz_b[i][j]  # Resta los elementos correspondientes
            fila.append(resta)  # Añade el resultado a la fila
        resta_resultado.append(fila)  # Añade la fila completa a la matriz de resultado
    return resta_resultado

# Multiplicación de matrices
def multiplicar_matrices (matriz_a, matriz_b):
    multiplicacion_resultado = []
    for i in range(len(matriz_a)):  # Recorre las filas de la primera matriz
        fila = []
        for j in range(len(matriz_b[0])):  # Recorre las columnas de la segunda matriz
            suma = 0
            for k in range(len(matriz_a[0])):  # Realiza la multiplicación de elementos y suma
                suma += matriz_a[i][k] * matriz_b[k][j]
            fila.append(suma)  # Añade el resultado a la fila
        multiplicacion_resultado.append(fila)  # Añade la fila completa a la matriz de resultado
    return multiplicacion_resultado

# Mostrar resultados
print("Suma de matrices:")
for fila in (sumar_matrices(matriz1, matriz2)):
    print(fila)

print("\nResta de matrices:")
for fila in (restar_matrices(matriz1, matriz2)):
    print(fila)

print("\nMultiplicación de matrices:")
for fila in (multiplicar_matrices(matriz1, matriz2)):
    print(fila)
