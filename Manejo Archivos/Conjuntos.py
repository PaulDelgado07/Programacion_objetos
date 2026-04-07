frutas = {"manzana","pera","limon", "naranja"}
citrus = {"naranja", "cebolla", "margarita"}

print(frutas.union(citrus))
print(frutas.intersection(citrus))
print(frutas.difference(citrus))

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

diferencia = conjunto1-conjunto2
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)