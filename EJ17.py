edades = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
lista_edad = list(edades)
for x in range(0, len(lista_edad)):
    lista_edad[x] = int(input("Ingrese una edad: "))
edades = tuple(lista_edad)
cant = 0
for x in edades:
    if x > 20:
        cant += 1
print(cant)
