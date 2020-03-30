def max_de_tres(n1, n2, n3):
    max = n1
    if n1 > n2 and n1 > n3:
        max = n1
    elif n2 > n3 and n2 > n3:
        max = n2
    else:
        max = n3
    return max


n1 = input("Ingrese un numero: ")
n2 = input("Ingrese un numero: ")
n3 = input("Ingrese un numero: ")

mayor = max_de_tres(n1, n2, n3)
print("El mayor es: " + str(mayor))
