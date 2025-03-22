# Tarea Semana 5 sobre la Implementación y Visualización de Algoritmos de Ordenamiento

# Sorting Algorithms Visualization

Este proyecto es una aplicación de visualización de algoritmos de ordenamiento escrita en Python utilizando la biblioteca Tkinter. Permite al usuario generar una lista aleatoria de números, elegir entre el algoritmo de Bubble Sort y Selection Sort, y visualizar el proceso de ordenamiento en tiempo real.

## Requisitos

- Python 3.x
- Tkinter (normalmente incluido con Python)
- ttkbootstrap (opcional para un tema de botón mejorado)

## Instalación

1. Clone el repositorio o descargue el archivo ZIP.
2. Asegúrese de tener Python instalado en su sistema.
3. Abra un terminal o Prompt de Comando y navegue hasta el directorio donde se encuentra el proyecto.
4. Ejecute el script principal `sorting_algorithms_visualization.py`.

## Uso

1. Inicie la aplicación y verá una ventana con un canvas en blanco, un menú desplegable para elegir el algoritmo, y tres botones: "Generar Tabla", "Iniciar" y "Reiniciar".
2. Haga clic en "Generar Tabla" para crear una lista aleatoria de números.
3. Elija el algoritmo de ordenamiento deseado en el menú desplegable.
4. Haga clic en "Iniciar" para comenzar el proceso de ordenamiento y verlo en tiempo real.
5. Haga clic en "Reiniciar" para limpiar el canvas y comenzar de nuevo.

## Personalización

- Para generar un mayor número de barras, modifique la función `generate()` y cambie el valor de `range(13)` a un número mayor.
- Para ajustar la velocidad de la animación, utilice el control deslizante "Select Speed [s]".

## Créditos

- El algoritmo de Bubble Sort y Selection Sort están implementados de manera estándar por Mayro Gameros 2890-23-11428.
- La visualización en tiempo real se logra con el uso de `time.sleep()` para pausar la ejecución entre iteraciones.

