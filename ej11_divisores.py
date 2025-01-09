numero = ""
while numero == "":
    try:    
        numero = int(input("Introduce un numero entero: "))
    except:
        print("Debes introducir un numero entero.")

lista_divisores = []

for divisor in range(1, numero + 1):
    resto = numero % divisor
    if resto == 0:
        lista_divisores.append(divisor)

print(f"Los divisores de {numero} son {lista_divisores}.")