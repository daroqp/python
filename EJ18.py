def empieza_con(letra, lista):
    cantidad = 0
    for word in lista:
        for x in word:
            if x == letra:
                cantidad += 1
    return cantidad


lista = ["daro", "daroska", "pepe", "juan", "maconia"]
letra = input("Ingrese la letra: ")

cant = empieza_con(letra, lista)
print(cant)
