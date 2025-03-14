#Crea una matriz pidiendo valores al usuario
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

#Imprime la matriz en forma de cadena
def imprimir_matriz(matriz):
    for fila in matriz:
        cadena_matriz = "|"
        
        for valor in fila:
            cadena_matriz += f"{valor} "

        cadena_matriz += "|"
        
        print(cadena_matriz)

#Recibe una matriz y devuelve su transpuesta
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

#Recibe dos matrices y devuelve su suma
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

#Devuelve el prdocuto de dos matrices del mismo tamaño
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

#Devuelve el prdocuto de dos matrices del mismo tamaño redondeando los resultados al decimal introducido en la tercera variable.
def producto_matrices_redondeado(m1,m2, indice_redondeo):
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
                    suma_de_de_valores_redondeada = round(suma_de_valores, indice_redondeo)
                    if indice_redondeo == 0:
                        suma_de_de_valores_redondeada = int(suma_de_de_valores_redondeada)
                
                lista_valores.append(suma_de_de_valores_redondeada)
            matriz_producto.append(lista_valores)

        return(matriz_producto)
