def aEntero(binario):
    cadena = str(binario)
    lista = list(reversed(cadena))
    index = 1
    entero = 0
    for x in lista:
        if x == '1':
            entero += index * 1
        index *= 2
    return entero


binario = 11110
print(aEntero(binario))
