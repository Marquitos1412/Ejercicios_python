from funciones_matrices import *

matriz_encriptadora = [[1,2,1],
                       [0,-1,3],
                       [2,1,0]]

#matriz_mensaje = pedir_matriz()

lista_valores = [" ","a","b","c","d","e","f",
                "g","h","i","j","k","l",
                "m","n","ñ","o","p","q",
                "r","s","t","u","v","w",
                 "x","y","z","."]

cadena = "flipped classroom."

lista = []

for valor in range(0, len(cadena)):
    indice = lista_valores.index(cadena[valor:valor+1])
    lista.append(indice)

print(f"{lista}")