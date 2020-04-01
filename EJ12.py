def mas_larga(lista):
    palarga = lista[0]
    larga = len(lista[0])
    for x in lista:
        if len(x) > larga:
            larga = len(x)
            palarga = x
    return palarga


lista = ["darou", "daro", "marcelDettmann", "dario", "darro"]
print(mas_larga(lista))
