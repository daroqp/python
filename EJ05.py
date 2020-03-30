def sum(lista):
    sumTotal = 0
    for number in lista:
        sumTotal += int(number)
    return sumTotal


def multip(lista):
    prodTotal = 1
    for number in lista:
        prodTotal *= int(number)
    return prodTotal


primerLista = []
salida = input(" 1 - Multiplicar:\n 2 - Sumar:\n S - Salir: ")
opcion = int(salida)
while salida != 's':
    primerLista.append(salida)
    salida = input("Ingrese un numero: ")
if opcion == 1:
    total = multip(primerLista)
    print(total)
if opcion == 2:
    total = sum(primerLista)
    print(total)
