import cv2
import numpy as np

img1 = cv2.imread("./ies-miralcamp-estudia-deporte.png")
filas = len(img1)
columnas = len(img1[0])

for fila in range(0, filas):
    for columna in range(0,columnas):
        if img1[fila,columna][0] != 255:
            img1[fila,columna] = (0,0,0)
            
        elif img1[fila,columna][1] != 255:
            img1[fila,columna] = (0,0,0)

        elif img1[fila,columna][2] != 255:
            img1[fila,columna] = (0,0,0)

#Mostrar imagenes
cv2.imshow('imagen-zeros',img1)

#Cerrar las ventanas con cualquier tecla 
cv2.waitKey(0)
cv2.destroyAllWindows()