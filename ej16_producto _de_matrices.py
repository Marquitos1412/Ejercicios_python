from funciones_matrices import *

def producto_matrices(m1,m2):
    if len(m1[0]) != len(m2):
        print("Las matrices deben ser del mismo tamaño.")
    
    else:
        numFilas_m1 = len(m1)
        numColumnas_m1 = len(m1[0])

        numColumnas_m2 = len(m2[0])

        matriz_producto = []

        for fila_m1 in range(0, numFilas_m1):
            lista_valores = []
            
            for columna_m2 in range(0, numColumnas_m2):
                suma_de_valores = 0
                
                for columna_m1 in range(0, numColumnas_m1):
                    suma_de_valores += m1[fila_m1][columna_m1] * m2[columna_m1][columna_m2]
                
                lista_valores.append(suma_de_valores)
            matriz_producto.append(lista_valores)

        return(matriz_producto)



m1 = pedir_matriz()
m2 = pedir_matriz()

matriz_producto = producto_matrices(m1,m2)
imprimir_matriz(matriz_producto)