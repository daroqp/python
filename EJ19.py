def contar_vocales(palabra):
    index = 0
    cont = [0, 0, 0, 0, 0]
    vocales = ['a', 'e', 'i', 'o', 'u']
    for x in vocales:
        for letra in palabra.lower():
            if letra == x:
                cont[index] += 1
        index += 1
    return cont


palabra = input("Ingrese una palabra: ")
vocales_totales = contar_vocales(palabra)
vocales = ['a', 'e', 'i', 'o', 'u']
for x in range(len(vocales)):
    print(vocales[x] + " : " + str(vocales_totales[x]))
