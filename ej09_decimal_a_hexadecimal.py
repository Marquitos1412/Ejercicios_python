es_numero_entero = False
while es_numero_entero == False:
    try:
        numero = int(input("Introduce el numero entero en base decimal a convertir: "))
        es_numero_entero = True
    except:
        print("El valor que has introducido no es un numero entero.")

lista_restos = []
dividendo = 1

while dividendo != 0:
    dividendo = numero // 16
    resto = numero % 16
    lista_restos.append(resto)
    numero = dividendo

numero_hexadecimal = ""

for valor in reversed(lista_restos):
    if valor == 10:
        numero_hexadecimal += "A"
    elif valor == 11:
        numero_hexadecimal += "B"
    elif valor == 12:
        numero_hexadecimal += "C"
    elif valor == 13:
        numero_hexadecimal += "D"
    elif valor == 14:
        numero_hexadecimal += "E"
    elif valor == 15:
        numero_hexadecimal += "F"
    else:
        numero_hexadecimal += f"{valor}"

print(f"El numero {numero} en hexadecimal es {numero_hexadecimal}.")
