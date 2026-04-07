# mi_tupla = (10, "hola", 3.14, [1,2,3,4])
# mi_tupla2 = list(mi_tupla)
# mi_tupla2.append(123)
# mi_tupla3 = tuple(mi_tupla2)

# print(mi_tupla3)

# t = (1,2,3,2,2)

# print(t.count(2))

# subtupla = t[1:]
# print(subtupla)

frase = input("Ingresa una frase: ")

# 1. Limpia la frase
limpia = frase.replace(",", "").replace(".", "").replace("?", "").replace("!", "").lower()

# 2. Separa en palabras
palabras = limpia.split()

# 3. Contar frecuencias
frecuencias = {}

for p in palabras:
    if p in frecuencias:
        frecuencias[p] += 1
    else:
        frecuencias[p] = 1

# 4. Ordenar de mayor a menor por frecuencia
ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

# 5. Mostrar resultados
for palabra, cantidad in ordenadas:
    print(f"{palabra}: {cantidad}")
