#region Raiz de 20
    #Importamos la funcion de la raiz cuadrada y calculamos la raiz de 20

from math import sqrt

raiz_20 = sqrt(20)

    #La comparamos con 5

comparacion_5 = raiz_20 > 5
print(f"¿Es la raiz de 20 mayor que 5?: {comparacion_5}")

    #La comparamos con 5 y con 4

comparacion_5_y_4 = 5 > raiz_20 > 4
print(f"¿Es la raiz de 20 mayor que 5?: {comparacion_5_y_4}")

#endregion

#region Circunferencia
    #Importamos el numero pi
from math import pi
    #Calculamos la longitud de las circunferencias de radios 5 y 0
longitud_circunferencia_radio_5 = 2 * pi * 5
longitud_circunferencia_radio_0 = 2 * pi * 0
    #Comparamos las longitud de radio 5 con 30
comparacion_longitud5 = longitud_circunferencia_radio_5 > 30
print(f"¿Es la longitud de la circunferencia de una esfera de radio 5 mayor que 30?: {comparacion_longitud5}")
print(f"¿Es la longitud de la circunferencia de una esfera de radio 0 mayor que 30?: {longitud_circunferencia_radio_0 == 0}")
#endregion

#region Nombre y caracteres
    #Primer nombre
nombre = input("Introduce tu nombre: ")
nombre_sin_espacios = nombre.replace(" ", "")
caracteres_nombre = len(nombre)
comparacion_nombre = 10 > caracteres_nombre > 5
print(f"¿Tiene mi nombre más de 5 caracteres y menos de 10?: {comparacion_nombre}")

    #Nombre completo
nombre_completo = input("Introduce tu nombre completo: ")
nombre_completo_sin_espacios = nombre_completo.replace(" ", "")
caracteres_nombre_completo = len(nombre_completo_sin_espacios)
comparacion_nombre_completo = 35 > caracteres_nombre_completo > 25
print(f"¿Tiene mi nombre completo más de 35 caracteres y menos de 25?: {comparacion_nombre_completo}")
#endregion
