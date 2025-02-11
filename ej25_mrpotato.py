import cv2
import numpy as np

img = cv2.imread("./lena.jpg")
lienzo = np.zeros((90,120,3), np.uint8)

ojo1 = img[240:290, 240:300]
ojo2 = img[240:290, 300:360]
boca = img[330:370, 240:360]

#Montar en el lienzo
filas_ojo1 = len(ojo1)

for fila in range(0, filas_ojo1):
    i = 0
    for pixel in ojo1[fila]:
        lienzo[fila,i] = pixel
        i += 1

filas_ojo2 = len(ojo2)

for fila in range(0, filas_ojo2):
    i = 60
    for pixel in ojo2[fila]:
        lienzo[fila,i] = pixel
        i += 1

filas_boca = len(boca)

for fila in range(0, filas_boca):
    i = 0
    for pixel in boca[fila]:
        lienzo[fila + 50,i] = pixel
        i += 1

#Mostrar imagenes
cv2.imshow('imagen', img)
cv2.imshow('lienzo', lienzo)
cv2.imshow('boca', boca)


#Cerrar las ventanas con cualquier tecla 
cv2.waitKey(0)
cv2.destroyAllWindows()