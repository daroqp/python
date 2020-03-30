def supos(ls1, ls2):
    for x in ls1:
        for y in ls2:
            if x == y:
                return True
    return False


ls1 = [1, 3, 5, 7, 8]
ls2 = [2, 4, 6, 8]

if supos(ls1, ls2):
    print("hay iguales")
else:
    print("no hay iguales")
