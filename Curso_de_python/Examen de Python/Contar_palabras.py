def contar_palabras(cadena):
    cadena = cadena.strip()
    if cadena == "":
        return 0
    return len(cadena.split())

print(contar_palabras("Python es un lenguaje de programación"))  # 5
print(contar_palabras("Hola"))                                   # 1
