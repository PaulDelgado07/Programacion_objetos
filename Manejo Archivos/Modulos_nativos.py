import math 
import statistics
datos = [10, 10, 8, 9, 6, 7, 4, 5]

media_aritmeticas = statistics.mean(datos)
valor_medio = statistics.median(datos)
moda = statistics.mode(datos)
print(f"Media aritmetica: {media_aritmeticas:.2f}")
print(f"Mediana {valor_medio:.2f}")
print(f"Moda es {moda:.2f}")

#numeros al azar 
import random
aleatorio = random.randint(1,10)
print(aleatorio)

#lista aleatoria
materia = ["matematicas", "lengua", "ciencias naturales", "fisica", "sociales"]
azar_materia = random.choice(materia)
print(azar_materia)


from datetime import datetime 
fecha_actual = datetime.now()

print(f"El dia de hoy es {fecha_actual.day} del mes de {fecha_actual.month} en el año {fecha_actual.year}")