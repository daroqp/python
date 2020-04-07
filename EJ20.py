def es_bisiesto(year):
    flag = False
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 != 0:
            flag = True
    return flag


year = input("Ingrese año: ")
if es_bisiesto(int(year)):
    print("Es bisiesto")
else:
    print("No es bisiesto")
