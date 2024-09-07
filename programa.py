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

def create_matrix():
    # Get the size of the matrix
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Initialize an empty matrix
    matrix = []

    print("Enter the elements row by row:")
    # Fill the matrix with user input
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    
    return matrix

# Example usage
matrix = create_matrix()
print("Matrix created:")
for row in matrix:
    print(row)


#Verificar si el numero de opcion es correcta
def verificar_opc(opc):
    if opc <= 0:
        opc = "Esa opcion no existe, ingrese una nueva"
    else:
        opc = "Opcion disponible, puede ingrsar esa opcion"
    return opc
    
    
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
#Seleccion de opcion
print ("Ingrese el numero de opcion de que desee realizar")
print("\n Opcion 2 = Suma de matrizes \n Opcion 3 = Resta de matrizes \n Opcion 4 = Multiplicacion de matrizes")
opcion = int(input())

if opcion == 1:
    opc = int(input())
    print (verificar_opc(opc))
elif opcion == 2:
    print("Suma de matrices:")
    for fila in (sumar_matrices(matriz1, matriz2)):
        print(fila)
  
elif opcion == 3:
    print("\nResta de matrices:")
    for fila in (restar_matrices(matriz1, matriz2)):
        print(fila)

elif opcion == 4:
    print("\nMultiplicación de matrices:")
    for fila in (multiplicar_matrices(matriz1, matriz2)):
        print(fila)
        
else:
    print ("Opcion no disponible")
    
    
    