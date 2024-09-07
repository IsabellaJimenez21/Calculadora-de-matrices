# Definición de matrices a usar

def crear_matriz():
    # Obtener el tamaño de la matriz
    filas = int(input("Ingresa el número de filas: "))
    columnas = int(input("Ingresa el número de columnas: "))

    # Inicializar una matriz vacía
    matriz = []

    print("Ingresa los elementos fila por fila:")
    # Llenar la matriz con la entrada del usuario
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingresa el elemento en la posición ({i+1}, {j+1}): "))
            fila.append(elemento)
        matriz.append(fila)
    
    return matriz


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
def menu ():
    print ("Ingrese el numero de opcion de que desee realizar")
    print("\n Opcion 2 = Suma de matrizes \n Opcion 3 = Resta de matrizes \n Opcion 4 = Multiplicacion de matrizes")
    opcion = int(input())
    
    print("Ingrese datos para la primera matriz")
    matriz1 = crear_matriz()
    print("Ingrese datos para la segundo matriz")
    matriz2 = crear_matriz()
    
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

menu()
    
    
    