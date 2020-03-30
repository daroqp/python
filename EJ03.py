def longitud(cadena):
    cont = 0
    for x in cadena:
        cont += 1
    return cont


cadena = input("Ingresar una cadena: ")

print("La palabra tiene un largo de: " + str(longitud(cadena)))
