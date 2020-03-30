def es_palindromo(cadena):
    fin = -1
    flag = False
    for x in range(len(cadena) // 2):
        if cadena[x] == cadena[fin]:
            flag = True
            fin -= 1
    return flag


palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("es palindromo")
else:
    print("no es palindromo")
