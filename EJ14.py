def cantMayus(palabra):
    cont = 0
    for x in palabra:
        if x.isupper():
            cont += 1
    return cont


palabra = input("Ingrese una cadena: ")
print(cantMayus(palabra))
