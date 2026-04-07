def invertir_cadena(cadena):
    resultado = ""
    for caracter in cadena:
        resultado = caracter + resultado
    return resultado

print(invertir_cadena("python"))
print(invertir_cadena("curso")) 
