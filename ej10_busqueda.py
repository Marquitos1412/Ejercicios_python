lista_valores = []
valor_lista = ""

while valor_lista != ".":
    valor_lista = input("Introduce un valor para la lista o un punto para terminar: ")
    if valor_lista != ".":
        lista_valores.append(valor_lista)

valor_busqueda = input("Introduce el valor que quieras buscar: ")

i = 0
valor_encotrado = False

for valor in lista_valores:
    if valor_busqueda == valor:
        print(f"Se ha encontrado el valor \"{valor_busqueda}\" en el indice {i} de la lista {lista_valores}.")
        valor_encotrado = True

    i += 1

if valor_encotrado == False:
    print(f"Se ha encontrado el valor \"{valor_busqueda}\" en el indice -1 de la lista {lista_valores}.")
