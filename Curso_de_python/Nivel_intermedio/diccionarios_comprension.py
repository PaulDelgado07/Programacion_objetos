"""
{clave_expr : calor_expr for item in iterable if condicion}
"""

cuadrados = {x:x**2 for x in range(5)}

#print(cuadrados)


cuadrados_pares = {x:x**2 for x in range(10) if x % 2==0 }
#print(cuadrados_pares)


diccionario = {"a":1, "b":2, "c":3}

diccionario_invertido = {v:k for k,v in diccionario.items()}
#print(diccionario_invertido)


tuplas =[("a", 1), ("b", 2), ("c", 3)]
diccionario = {k:v for k,v in tuplas}
print(diccionario)
