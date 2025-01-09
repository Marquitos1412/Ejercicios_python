caracter = input("Introduce un unico caracter: ")

while len(caracter) > 1:
    print("Solo puedes introducir un solo caracter.")
    caracter = input("Introduce un unico caracter: ")

if "A" >= caracter >= "Z":
    print(f"El caracter {caracter} es una mayuscula.")

elif "a" >= caracter >= "z":
    print(f"El caracter {caracter} es una minuscula.")

else:
    print(f"{caracter} no es una letra.")
