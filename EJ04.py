def isVocal(char):
    flag = False
    vocal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for x in vocal:
        if x == char:
            flag = True
    return flag


letra = input("Ingrese un caracter: ")

print(isVocal(letra))
