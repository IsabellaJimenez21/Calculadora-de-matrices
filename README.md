# Calculadora de Matríces

## Conceptos incluidos en el programa
Uso de matrices para que los usuarios realicen operaciones aritméticas con ellas, estructuras de control para los menús, ciclos para que el usuario ingrese los datos, realizar las operaciones entre matrices y funciones para separar y hacer reutilizable el código. 

## ¿Qué son las matrices?
Las matrices son arreglos bidimensionales de elementos que están en filas y columnas. Son una herramienta fundamental en matemáticas y se utilizan en diferentes áreas como álgebra lineal, física, ingeniería, y ciencias de la computación. En una matriz, cada elemento puede ser identificado por su posición, que se indica mediante un par de índices: el número de fila y el número de columna.

## Operaciones Básicas con Matrices:

### Suma y Resta de Matrices:
La suma y resta de matrices son operaciones elementales que se realizan elemento a elemento. Para sumar o restar dos matrices, ambas deben tener las mismas dimensiones (mismo número de filas y columnas). Estas operaciones son útiles en la resolución de sistemas de ecuaciones y en el procesamiento de señales.

### Multiplicación de Matrices:
La multiplicación de matrices es una operación un poco más compleja. Para multiplicar dos matrices, el número de columnas de la primera matriz debe coincidir con el número de filas de la segunda. Esta operación es crucial en transformaciones lineales, gráficos por computadora, y en la representación y resolución de sistemas de ecuaciones lineales.

### Transposición de una Matriz:
Transponer una matriz implica cambiar sus filas por columnas. Esta operación es útil en muchas cosas, como en el cálculo de determinantes y en la teoría de sistemas lineales.

## ¿Por qué es interesante aprender estas operaciones?

Para mi el entender y manejar matrices junto con sus operaciones es muy importante para áreas avanzadas de matemáticas y computación. Entender las matrices me permitirá representar y manipular datos de manera eficiente, algo que es crucial en la programación cuando se trabaja con gráficos, inteligencia artificial, y algoritmos de machine learning.

## Aplicaciones Prácticas:

### Resolución de Sistemas de Ecuaciones:
Las matrices se utilizan para resolver sistemas de ecuaciones lineales, que aparecen en diversas disciplinas como la economía, la ingeniería y las ciencias sociales.

Fuentes: https://revistas.udistrital.edu.co/index.php/vinculos/article/view/11660/12869#:~:text=El%20software%20calculador%20de%20matrices,verificar%20si%20una%20matriz%20tiene
https://es.quora.com/C%C3%B3mo-se-aplican-las-matrices-en-la-vida-real
https://www.slideshare.net/slideshow/matrices-en-la-vida-cotidiana/123743231


# Algoritmo 
## 1. Inicio del Programa:
El programa comienza mostrando un menú principal donde se presentan varias opciones. Este menú permite que el usuario seleccione la operación que desee entre: suma de matrices, resta de matrices, multiplicación de matrices, promedio de una matriz, o salir del programa.

## 2. Elección de Operación:
Despues, se le pedira al usuario que elija la operación que quiera realizar ingresando el número correspondiente a la opción en el menú. Una vez ingresada la opción, el programa verifica que sea válida, lo que significa que corresponda a una de las operaciones que están disponibles. Si el número ingresado no es válido, se le pedirá al usuario que lo intente nuevamente hasta que seleccione una opción que sea correcta.

## 3. Ingreso de Matrices:
Dependiendo de la operación seleccionada, el programa solicita las dimensiones de las matrices involucradas. Por ejemplo, para las operaciones de suma, resta o multiplicación de matrices, se piden las dimensiones de dos matrices. En el caso del promedio, solo se solicita la dimensión de una matriz. Posteriormente, el programa valida que las dimensiones ingresadas sean compatibles con la operación que se quiera realizar. Por ejemplo, para la suma o resta, se verifica que las matrices tengan las mismas dimensiones, mientras que para la multiplicación, se comprueba que el número de columnas de la primera matriz coincida con el número de filas de la segunda.

## 4. Llenado de Matrices:
Después de validar las dimensiones, el usuario procede a ingresar los valores de cada matriz, fila por fila. Estos valores se almacenan en listas que tienen listas, con cada fila de la matriz representada por una lista dentro de otra lista más grande. Las matrices se guardan de esta manera para poder ser procesadas en las operaciones seleccionadas.

## 5. Realización de la Operación:
El programa realiza la operación seleccionada por el usuario. En el caso de la suma de matrices, se suman elemento por elemento de las dos matrices ingresadas. Para la resta, se restan los elementos correspondientes de ambas matrices. Si se selecciona la multiplicación, el programa lleva a cabo una multiplicación de las dos matrices. Finalmente, si se elige el promedio, se genera una nueva matriz en la que se suman los elementos y se restan entre el número de estos.

## 6. Mostrar Resultado:
Tras realizar la operación, el programa muestra en pantalla la matriz resultante. Esta matriz es el producto de la operación seleccionada, y se presenta al usuario para que pueda revisarla.

## 7. Repetir o Finalizar: 
Finalmente, el programa pregunta al usuario si desea realizar otra operación o si prefiere salir. Si el usuario decide realizar otra operación, se regresa al menú principal o de inicio, permitiéndo que seleccione otra vez entre las distintas opciones disponibles. Si el usuario elige salir, el programa termina su ejecución y finaliza.
