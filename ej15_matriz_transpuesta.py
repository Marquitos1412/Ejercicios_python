from funciones_matrices import *

def matriz_transpuesta(matriz):
    matriz_transpuesta = []
    numFilas = len(matriz)
    numColumnas = len(matriz[0])

    for columna in range(0, numColumnas):
        lista_valores = [] #Lista de valores que se introduce en la matriz

        for fila in range(0, numFilas):
            valor = matriz[fila][columna]
            lista_valores.append(valor)

        matriz_transpuesta.append(lista_valores)

    return(matriz_transpuesta)

imprimir_matriz(matriz_transpuesta(pedir_matriz()))

