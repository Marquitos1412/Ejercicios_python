parcial_1 = float(input("Introduce la nota del primer parcial: "))
parcial_2 = float(input("Introduce la nota del segundo parcial: "))
parcial_3 = float(input("Introduce la nota del tercer parcial: "))

media_parciales = (parcial_1+parcial_2+parcial_3) / 3
media_parciales_redondeada = round(media_parciales, 2)

if parcial_1 < 3 or parcial_2 < 3 or parcial_3 < 3:
    print("Has suspendido. Una de tus notas es inferior a 3.")

elif media_parciales < 5:
    print(f"Has supendido. La media de tus notas, {media_parciales_redondeada}, es inferior a 5.")

else:
    print(f"Has aprobado. Tu nota media es un {media_parciales_redondeada}.")

