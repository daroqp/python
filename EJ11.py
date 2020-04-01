def max_in_list(lista):
    mayor = lista[0]
    for x in lista:
        if x > mayor:
            mayor = x
    return mayor


lista = [9, 4, 2, 6, 3, 10]
print(max_in_list(lista))
