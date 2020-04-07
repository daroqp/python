def calcul_edad(ageNow, age):
    return ageNow - age


person = {
    "name": "none",
    "year": 0
}

year = input("Ingrese año actual: ")
person["name"] = input("Ingrese el nobre: ")
person["year"] = input("Ingrese el año de nacimiento: ")

edad = calcul_edad(int(year), int(person.get("year")))
print("La edad es: " + str(edad))
