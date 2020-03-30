def maxima(n1, n2):
    x = 0
    if n1 > n2:
        x = n1
    else:
        x = n2
    return x


numero1 = input("Ingrese el primer numero: ")
numero2 = input("Ingrese el segundo numero: ")

nmax = maxima(numero1, numero2)

print("El numero mas alto es: " + str(nmax))
