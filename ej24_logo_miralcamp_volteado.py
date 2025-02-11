import cv2
import numpy as np

img = cv2.imread("./ies-miralcamp-estudia-deporte.png")
filas = len(img)
columnas = len(img[0])


def rotar_imagen(img):
    img_volteada = np.zeros((filas, columnas, 3),np.uint8)

    for fila in range(0,filas):
        for columna in range(0, columnas):
            img_volteada[fila, columnas-columna-1] = img[fila, columna]

    return(img_volteada)

img_volteada = rotar_imagen(img)

#Mostrar imagenes
cv2.imshow('imagen-rotada', img_volteada)

#Cerrar las ventanas con cualquier tecla 
cv2.waitKey(0)
cv2.destroyAllWindows()