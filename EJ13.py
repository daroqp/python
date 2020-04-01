def filtrar_palabra(lista, n):
    for x in lista:
        if len(x) == n:
            print(x)


lista = ["daro", "daro", "darox", "xdaro", "dettmann"]
filtrar_palabra(lista, 4)
