def inversa(cadena):
    lista = list(cadena)
    invert = ""
    while lista:
        neWord = lista.pop()
        invert += neWord
    return invert


palabra = input("Ingresee una palabra: ")
print(inversa(palabra))
