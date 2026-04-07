#Eliminar duplas diplicadas
# lista = [1, 2, 2, 3, 3, 4]
# conjunto = set(lista)
# lista_sin_duplicados = list(conjunto)
# print(lista_sin_duplicados)

#Econtrar elementos comunes en dos conjuntos

conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8}

def elementos_comunes(conjunto1, conjunto2):
    return conjunto1 & conjunto2

# print(elementos_comunes(conjunto1,conjunto2))