def generarCaracteres(x, y):
    generada = ""
    while x > 0:
        generada += y
        x -= 1
    return generada


def otroG(n, x):
    return n * x


palabra = generarCaracteres(3, "x")
print(palabra)

otra = otroG(3, "x")
print(otra)
