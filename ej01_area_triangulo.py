#Recibe los valores de la base y la altura y los convierte en float.

base = float(input("Introduzca el valor de la base del triangulo: "))
altura = float(input("Introduzca el valor de la altura del triangulo: "))

#Calcula el area del triangulo y la redondea a dos digitos.

area = round(base * altura, 2)

#Escribe la respuesta.

print(f"El area del triangulo es de {area}m cuadrados")
