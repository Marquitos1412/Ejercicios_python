import cv2
import numpy as np

#Crea arreglos que son la base de una imagen
img1 = np.zeros((6,8,3),np.uint8)
img2 = 255*np.ones((6,8,3),np.uint8)

#Establecer 4 píxeles colores en img fondo negro
img1[1, 1] = (50 , 50 , 50)
img1[4, 4] = (200 , 150 ,10)
img1[3, 5] = (75, 100, 255)
img1[2, 3] = (255, 50 , 100)
 
#Establecer 4 píxeles colores en img fondo blanco
img2[1, 1] = (0 , 255 , 255)
img2[4, 4] = (30 , 50 ,255)
img2[3, 5] = (255, 255, 50)
img2[5, 7] = (150, 250 , 50)

#Mostrar imagenes
cv2.imshow('imagen-zeros',img1)
cv2.imshow('imagen-blanca',img2)

#Cerrar las ventanas con cualquier tecla 
cv2.waitKey(0)
cv2.destroyAllWindows()