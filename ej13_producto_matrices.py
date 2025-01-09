def pedir_matriz():
    matriz = []

    filas = ""
    columnas = ""

#Bucle que pide el nº de filas y columnas de la matriz
    while filas == "" or columnas == "":
        if filas == "":
            try:    
                filas = int(input("Introduce un numero entero de filas: "))
            except:
                print("Debes introducir un numero entero de filas.")

        if columnas == "":
            try:    
                columnas = int(input("Introduce un numero entero de columnas: "))
            except:
                print("Debes introducir un numero entero de columnas.")

#Bucle que crea la matriz
    for fila in range(0, filas):
        lista_valores = [] #Lista de valores que se introduce en la matriz

        for columna in range(0, columnas):

            valor = "" #Valor que se introduce en la lista de valores

            while valor == "":
                    try:
                        valor = int(input(f"Introduce un valor para la posicion ({fila},{columna}): "))
                    except:
                        print("Debes introducir un numero entero como valor.")
            
            lista_valores.append(valor)
        
        matriz.append(lista_valores)

    return(matriz)

def imprimir_matriz(matriz):
    for fila in matriz:
        cadena_matriz = "|"
        
        for valor in fila:
            cadena_matriz += f"{valor}"

        cadena_matriz += "|"
        
        print(cadena_matriz)

imprimir_matriz(pedir_matriz())