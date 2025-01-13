from funciones_matrices import *

def suma_matrices(m1,m2):

    imprimir_matriz(m1)
    print("+")
    imprimir_matriz(m2)
    print("=")


    matrices_iguales = True

    numFilas = len(m1)

    if len(m1) == len(m2):
        for fila in range(0, numFilas):
            if len(m1[fila]) != len(m2[fila]):
                matrices_iguales = False
                break

    else:
        matrices_iguales = False    

    matriz_suma = []
    numColumnas = len(m1[0])

    if matrices_iguales == True:
        for fila in range(0, numFilas):
            lista_valores = [] #Lista de valores que se introduce en la matriz

            for columna in range(0, numColumnas):
                valor_suma = m1[fila][columna] + m2[fila][columna]
                
                lista_valores.append(valor_suma)
            
            matriz_suma.append(lista_valores)

        imprimir_matriz(matriz_suma)

    else:
        print("No son del mismo tamaño.")

print("Introduce la primera matriz:")
m1 = pedir_matriz()
print("Introduce la segunda matriz:")
m2 = pedir_matriz()

suma_matrices(m1,m2)
