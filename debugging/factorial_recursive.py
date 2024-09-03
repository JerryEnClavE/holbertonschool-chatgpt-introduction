#!/usr/bin/python3
import sys  # Importa el módulo sys para manejar los argumentos de línea de comandos

def factorial(n):
    """
    Calcula el factorial de un número de manera recursiva.
    
    Args:
        n (int): El número entero para el cual se quiere calcular el factorial.

    Returns:
        int: El factorial de n. Si n es 0, devuelve 1, ya que 0! = 1.
    """
    if n == 0:
        return 1  # Caso base: el factorial de 0 es 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva para calcular el factorial de n-1

# Convierte el argumento pasado por línea de comandos a un entero
# sys.argv[1] es el primer argumento después del nombre del script
f = factorial(int(sys.argv[1]))

# Imprime el resultado del cálculo del factorial
print(f)