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
suma_resultado = []
for i in range(len(matriz1)):  # Recorre las filas de la matriz
    fila = []
    for j in range(len(matriz1[i])):  # Recorre las columnas de la matriz
        suma = matriz1[i][j] + matriz2[i][j]  # Suma los elementos correspondientes
        fila.append(suma)  # Añade el resultado a la fila
    suma_resultado.append(fila)  # Añade la fila completa a la matriz de resultado

# Resta de matrices
resta_resultado = []
for i in range(len(matriz1)):  # Recorre las filas de la matriz
    fila = []
    for j in range(len(matriz1[i])):  # Recorre las columnas de la matriz
        resta = matriz1[i][j] - matriz2[i][j]  # Resta los elementos correspondientes
        fila.append(resta)  # Añade el resultado a la fila
    resta_resultado.append(fila)  # Añade la fila completa a la matriz de resultado

# Multiplicación de matrices
multiplicacion_resultado = []
for i in range(len(matriz1)):  # Recorre las filas de la primera matriz
    fila = []
    for j in range(len(matriz2[0])):  # Recorre las columnas de la segunda matriz
        suma = 0
        for k in range(len(matriz1[0])):  # Realiza la multiplicación de elementos y suma
            suma += matriz1[i][k] * matriz2[k][j]
        fila.append(suma)  # Añade el resultado a la fila
    multiplicacion_resultado.append(fila)  # Añade la fila completa a la matriz de resultado

# Mostrar resultados
print("Suma de matrices:")
for fila in suma_resultado:
    print(fila)

print("\nResta de matrices:")
for fila in resta_resultado:
    print(fila)

print("\nMultiplicación de matrices:")
for fila in multiplicacion_resultado:
    print(fila)
