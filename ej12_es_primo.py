numero = ""
while numero == "":
    try:    
        numero = int(input("Introduce un numero entero: "))
    except:
        print("Debes introducir un numero entero.")

num_divisores = 0

for divisor in range(1, numero + 1):
    resto = numero % divisor
    if resto == 0:
          num_divisores += 1

if num_divisores > 2:
    print(f"El numero {numero} no es primo.")
else:
    print(f"El numero {numero} es primo.")