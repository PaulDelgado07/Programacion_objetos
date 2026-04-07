"""🧠 Ejercicio sencillo: Asistencia de un solo día
🎯 Objetivo:
Pedir nombres de varios estudiantes

Preguntar si asistieron hoy

Mostrar al final quiénes asistieron y quiénes no"""

presentes = [] 
ausentes = []

cantidad = int(input("Ingrese la cantidad de los estudiantes: "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre de los estudiantes: ")
    estado = input("¿Asistió hoy? (s/n)")

    if estado.lower() == 's':
        presentes.append(nombre)
    else: 
        presentes.append(nombre)
        
print("Presentes: ")
for nombre in presentes: 
    print("-", nombre)

print("Ausentes: ")
for nombre in ausentes: 
    print("-", nombre)    