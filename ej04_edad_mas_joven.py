edad_persona_1 = int(input("Introduce la edad de la primera persona: "))
edad_persona_2 = int(input("Introduce la edad de la segunda persona: "))

if edad_persona_1 < edad_persona_2:
    print("La primera persona es mas joven que la segunda.")

elif edad_persona_2 < edad_persona_1:
    print("La segunda persona es mas joven que la primera.")

else:
    print("Ambas personas tienen la misma edad.")
