import cv2
import numpy as np

img1 = cv2.imread("./ies-miralcamp-estudia-deporte.png")
filas = len(img1)
columnas = len(img1[0])

for fila in range(0, 123):
    for columna in range(0,columnas):
    #Rojo
        if img1[fila,columna][2] == 219 or img1[fila,columna][2] == 217 or img1[fila,columna][2] == 230:
            img1[fila,columna] = (255,0,255)
    #Amarillo        
        elif img1[fila,columna][2] == 250 or img1[fila,columna][2] == 251 or img1[fila,columna][2] == 252:
            img1[fila,columna] = (255,0,0)
    #Verde        
        elif img1[fila,columna][2] == 138 or img1[fila,columna][2] == 131 or img1[fila,columna][2] == 177:
            img1[fila,columna] = (0,0,30)
    #Azul        
        elif img1[fila,columna][2] == 46 or img1[fila,columna][2] == 34 or img1[fila,columna][2] == 116:
            img1[fila,columna] = (0,255,125)

#Mostrar imagenes
cv2.imshow('imagen-zeros',img1)

#Cerrar las ventanas con cualquier tecla 
cv2.waitKey(0)
cv2.destroyAllWindows()