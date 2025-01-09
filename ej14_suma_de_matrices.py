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

m1 = pedir_matriz()
m2 = pedir_matriz()

matriz_suma = []

matrices_iguales = True

if len(m1) == len(m2):
    numFilas = len(m1)
    for fila in range(0, numFilas):
        if len(m1[fila]) != len(m2[fila]):
            matrices_iguales = False

if matrices_iguales == True:
    for fila in m1:
        for valor_m1 in fila:
            #valor_suma = valor_m1 +
            print()
else:
    print("No son del mismo tamaño.")