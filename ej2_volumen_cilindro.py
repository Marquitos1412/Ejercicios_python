#Importamos el numero pi

from math import pi

#Recibe los valores del radio y la altura y los convierte en float.

radio = float(input("Introduzca el valor del radio del cilindro: "))
altura = float(input("Introduzca el valor de la altura del cilindro: "))

#Calcula el volumen del cilindro y la redondea a dos digitos.

volumen = pi * radio**2 * altura
volumen_redondeado = round(volumen, 2)

#Escribe la respuesta.

print(f"El volumen del cilindro es de {volumen_redondeado} cubicos")