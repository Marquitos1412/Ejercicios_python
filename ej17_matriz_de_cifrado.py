from funciones_matrices import *

matriz_encriptadora = [[1,2,1],
                       [0,-1,3],
                       [2,1,0]]

inversa_matriz_encriptadora = [[-3/11,1/11,7/11],
                               [6/11,-2/11,-3/11],
                               [2/11,3/11,-1/11]]

lista_valores = [" ","a","b","c","d","e","f",
                "g","h","i","j","k","l",
                "m","n","ñ","o","p","q",
                "r","s","t","u","v","w",
                 "x","y","z","."]

def cifrar_mensaje(mensaje):

    #region Traduce el mensaje a matriz

    resto = len(mensaje) % 3

    while resto != 0:

        mensaje += " "

        resto = len(mensaje) % 3

    matriz_traducida = []

    lista_columna = []

    i = 0

    for valor in range(0, len(mensaje)):
        if i == 3:
            i = 0
            matriz_traducida.append(lista_columna)
            lista_columna = []
        
        indice = lista_valores.index(mensaje[valor:valor+1])
        lista_columna.append(indice)

        i += 1

        if valor == len(mensaje) - 1:
            matriz_traducida.append(lista_columna)

    #endregion

    #region Encripta la matriz con la matriz encriptadora

    matriz_encriptada = []
    
    for fila in matriz_traducida:
        lista_operar = []
        lista_operar.append(fila)

        fila_encriptada = producto_matrices(lista_operar, matriz_encriptadora)
        matriz_encriptada.append(fila_encriptada[0])

    #endregion

    return(matriz_encriptada)


def descifrar_mensaje(matriz_encriptada):
    #Desencripta la matriz y devuelve la matriz inicial
    matriz_desencriptada = []

    for fila in matriz_encriptada:
        matriz_fila = []
        matriz_fila.append(fila)

        fila_desencriptada = producto_matrices_redondeado(matriz_fila, inversa_matriz_encriptadora, 0)
        matriz_desencriptada.append(fila_desencriptada[0])

    mensaje_desencriptado = ""

    for fila in matriz_desencriptada:
        for valor in fila:
            mensaje_desencriptado += lista_valores[valor]

    return(mensaje_desencriptado)

mensaje = input("Introduce el mensaje que se cifrara: ")

a = cifrar_mensaje(mensaje)

imprimir_matriz(a)
print("------------")
b = descifrar_mensaje(a)

print(b)