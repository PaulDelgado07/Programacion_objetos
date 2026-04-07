def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    
    return lista_sin_duplicados

print(eliminar_duplicados([1, 2, 2, 3, 4, 4]))
print(eliminar_duplicados([5, 5, 5, 6, 7]))    
