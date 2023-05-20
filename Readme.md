# Repositorio para test de metodos de Ordenamiento

### Metodos empleados para el test:

- Bubble Sort (Ordenamiento de Burbuja): Es un método simple pero ineficiente. Consiste en comparar elementos adyacentes y intercambiarlos si están en el orden incorrecto. Este proceso se repite hasta que la matriz esté completamente ordenada.

- Bucket Sort (Ordenamiento de Cubetas): Este método se basa en dividir la matriz en un número finito de "cubetas" o baldes. Cada cubeta se ordena individualmente, y luego se combinan todas las cubetas para obtener la matriz final ordenada.

- Heap Sort (Ordenamiento por Montículos): Utiliza una estructura de datos llamada montículo (heap) para organizar los elementos. Se construye un montículo a partir de la matriz desordenada y se extraen los elementos en orden, asegurando que el montículo se mantenga ordenado en cada paso.

- Insertion Sort (Ordenamiento por Inserción): En este método, se construye una matriz ordenada desde el principio y se insertan elementos no ordenados en su posición adecuada. Se compara cada elemento con los elementos previos de la matriz ordenada y se inserta en su lugar correspondiente.

- Quick Sort (Ordenamiento Rápido): También conocido como "Quicksort", es uno de los métodos más populares y eficientes. Se elige un elemento pivote y se reorganizan los elementos de la matriz de manera que los elementos menores al pivote estén a su izquierda y los mayores estén a su derecha. Luego, se aplica el mismo proceso de forma recursiva a las submatrices antes y después del pivote.

- Selection Sort (Ordenamiento por Selección): En este método, se selecciona repetidamente el elemento más pequeño de la matriz y se coloca en su posición correcta. Se realiza un recorrido completo de la matriz, encontrando el elemento mínimo en cada iteración.

- Shell Sort (Ordenamiento de Shell): Se basa en una estrategia de comparación y intercambio de elementos distantes entre sí, utilizando una secuencia de brechas predefinidas. A medida que se reducen las brechas, se realiza un ordenamiento más refinado, hasta que finalmente se obtiene la matriz ordenada.

### Como realizar el test?

Una vez clonado el repositorio ingrese la siguiente linea de comandos en consola
`py .\test.py`
