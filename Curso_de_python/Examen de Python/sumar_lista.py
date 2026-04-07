def sumar_lista(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

print(sumar_lista([1, 2, 3, 4]))    # 10
print(sumar_lista([5, 10, 15]))     # 30

