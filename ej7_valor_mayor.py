lista_valores = []

i = 0

while i < 5:
    print(f"Has introducido {i} numeros.")
    try:
        num_anadido = int(input(f"Introduce el siguiente numero: "))
        lista_valores.append(num_anadido)
        i += 1
    except:
        print("No es un numero.")

valor_mayor = 0

for valor in lista_valores:
    if valor > valor_mayor:
        valor_mayor = valor

print(f"El numero mas grande de los que has introducido {lista_valores} es {valor_mayor}.")