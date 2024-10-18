"""
Proyecto Python
Calculadora de matrices.
El programa funciona como una calculadora que da la opción de sumar, 
restar y multiplicar dos matrices entre sí,
además de calcular el promedio de una matriz, las cuales son proporcionadas por un usuario. 
El programa devuelve el resultado de estas operaciones en una matriz nueva. 
"""
"""
================== Funcion de validar opcion =====================================
"""

# Verificar si la opción ingresada es un número válido y está en el rango de opciones
def verificar_opc(opc):
    """
    (uso de funciones y de condicionales)
    recibe: opc como string
   valida si la opción es un número entero dentro del límite de opciones
    devuelve: True si la opción es válida, False en caso contrario
    """
    try:
        opc = int(opc)  # Intentar convertir a entero
    except ValueError:
        print("Eso no es un número. Por favor, ingrese una opción válida.")
        return False

    if opc in [1, 2, 3, 4, 5]:
        print("Opción disponible, puede ingresar esa opción.")
        return True
    else:
        print("Esa opción no existe, ingrese una nueva.")
        return False
"""
================== Función de definir matrices  =====================================
"""
def crear_matriz():
    """
    (uso de funciones, listas anidadas, ciclos y ciclos anidados)
    recibe: filas valor numérico, columnas valor numérico
    crea una matriz
    devuelve: una matriz con valores, número de filas y columnas proporcionados por el usuario
    """
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
    
"""
================== Funciones de operaciones  =====================================
"""
    
# Suma de matrices
def sumar_matrices (matriz_a, matriz_b):
    """
    (uso de operadores, funciones, listas anidadas, ciclos y ciclos anidados)
    recibe: matriz_a lista anidada, matriz_b lista anidada
    suma dos matrices
    devuelve: el resultado de la suma en una nueva matriz
    """
    suma_resultado = []  
    # Recorre las filas de la matriz
    for i in range(len(matriz_a)):  
        fila = []
        # Recorre las columnas de la matriz
        for j in range(len(matriz_a[i])):  
            # Suma los elementos correspondientes
            suma = matriz_a[i][j] + matriz_b[i][j]  
            # Añade el resultado a la fila
            fila.append(suma)  
        # Añade la fila completa a la matriz de resultado
        suma_resultado.append(fila) 
    return suma_resultado


# Resta de matrices
def restar_matrices (matriz_a, matriz_b):
    """
    (uso de operadores, funciones, listas anidadas, ciclos y ciclos anidados)
    recibe: matriz_a lista anidada, matriz_b lista anidada
    resta dos matrices
    devuelve: el resultado de la resta en una nueva matriz
    """
    resta_resultado = []
    # Recorre las filas de la matriz
    for i in range(len(matriz_a)):  
        fila = []
        # Recorre las columnas de la matriz
        for j in range(len(matriz_a[i])):
            # Resta los elementos correspondientes
            resta = matriz_a[i][j] - matriz_b[i][j]  
            # Añade el resultado a la fila
            fila.append(resta)  
        # Añade la fila completa a la matriz de resultado
        resta_resultado.append(fila)  
    return resta_resultado


# Multiplicación de matrices
def multiplicar_matrices (matriz_a, matriz_b):
    """
    (uso de operadores, funciones, listas anidadas, ciclos y ciclos anidados)
    recibe: matriz_a lista anidada, matriz_b lista anidada
    multiplica dos matrices
    devuelve: el resultado de la multiplicación en una nueva matriz
    """
    multiplicacion_resultado = []
    # Recorre las filas de la primera matriz
    for i in range(len(matriz_a)):  
        fila = []
        # Recorre las columnas de la segunda matriz
        for j in range(len(matriz_b[0])):  
            suma = 0
            # Realiza la multiplicación de elementos y suma
            for k in range(len(matriz_a[0])):  
                suma += matriz_a[i][k] * matriz_b[k][j]
            # Añade el resultado a la fila
            fila.append(suma)
        # Añade la fila completa a la matriz de resultado
        multiplicacion_resultado.append(fila) 
    return multiplicacion_resultado


def promedio_matriz(matriz):
    """
    (uso de operadores, funciones, listas anidadas, ciclos y ciclos anidados)
    recibe: matriz lista anidada
    calcula el promedio de una matriz
    devuelve: el resultado del promedio de una matriz en valor numérico
    """
    acum = 0
    cont_num = 0
    for fila in (matriz):
        for num in fila:
            acum = acum + num
            cont_num = cont_num + 1
    return acum/cont_num
    
"""
================== Funcion de opciones  =====================================
"""

# Mostrar resultados
#Seleccion de opcion
def menu ():
    """
    (funciones, condicionales, ciclos y ciclos anidados)
    recibe: opcion valor numerico
    dependiendo la opcion seleccionada ejecuta la operacion correspondiente
    devuelve: el resultado de la operación seleccionada
    """
    while True:
        print ("Ingrese el número de opción que desee realizar")
        print("Opción 1 = Suma de matrizes \nOpción 2 = Resta de matrizes")
        print ("Opción 3 = Multiplicación de matrizes \nOpción 4 = Promedio de matriz \nOpción 5 = Detener")     
       
        # Mantener como string para validar
        opcion = input()  

        # Validar opción antes de continuar
        if  not verificar_opc(opcion):
            continue

        # Convertir la opción validada a entero
        opcion = int(opcion)
        
  
        if opcion == 1:
            print("Ingrese datos para la primera matriz")
            matriz_1 = crear_matriz()
            print("Ingrese datos para la segunda matriz")
            matriz_2 = crear_matriz()
        
            print("Suma de matrices:")
            for fila in (sumar_matrices(matriz_1, matriz_2)):
                print(fila)
        
        elif opcion == 2:
            print("Ingrese datos para la primera matriz")
            matriz_1 = crear_matriz()
            print("Ingrese datos para la segunda matriz")
            matriz_2 = crear_matriz()
        
            print("\nResta de matrices:")
            for fila in (restar_matrices(matriz_1, matriz_2)):
                print(fila)

        elif opcion == 3:
            print("Ingrese datos para la primera matriz")
            matriz_1 = crear_matriz()
            print("Ingrese datos para la segunda matriz")
            matriz_2 = crear_matriz()
        
            print("\nMultiplicación de matrices:")
            for fila in (multiplicar_matrices(matriz_1, matriz_2)):
                print(fila)
                
        elif opcion == 4:
            print ("Ingresa datos para tu matriz")
            matriz = crear_matriz()
        
            print ("\nPromedio de matriz:")
            print (promedio_matriz(matriz))
        # Opcion para detener el programa        
        elif opcion == 5:
            break
            
        else:
            print ("Opción no disponible")

menu()
    
    
    