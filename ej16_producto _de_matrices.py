def producto_matrices(m1,m2):
    if len(m1) != len(m2):
        print("Las matrices deben ser del mismo tamaño.")
    
    elif len(m1[0]) != len(m2[0]):
        print("Las matrices deben ser del mismo tamaño.")
    
    else:
        numFilas = len(m1)
        numColumnas = len(m1[0])

        for fila in range(0, numFilas):
            print("")
