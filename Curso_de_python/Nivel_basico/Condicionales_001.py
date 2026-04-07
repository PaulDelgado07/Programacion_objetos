""""
x = 0

if x > 0:
    print("Es mayor a cero")
elif x == 0: 
    print("Es igual que cero")
else: 
    print("Es menor que 0")
"""
# try: 
#     nota1 = float(input("Ingrese la primera nota: "))
#     nota2 = float(input("Ingrese la segunda nota: "))
#     nota3 = float(input("Ingrese la tercera nota: "))

#     promedio = (nota1 + nota2 + nota3)/3

#     if promedio >= 7: 
#         print(f"aprobado con un promedio de: {promedio:.2f}")
#     else:
#         print(f"Reprobado con un promedio de: {promedio:.2f}")
#         print("Pero para mejorar el promedio...")
#         nota_sustitutoria = float(input("Ingrese la nota sustitutoria: "))
#         promedio_supletorio = (nota_sustitutoria + promedio)/2
#         if promedio_supletorio >= 7: 
#             print(f"Aprobaste con un promedio de: {round(promedio_supletorio,2)}")
#         else: 
#             print(f"Reprobaste materia, repites año")

# except ValueError: 
#     print("No ingrese letras, ingrese numeros.")

# computadora = float(input("Ingrese el costo del la computadora: "))

# IVA = 0.25 

# if computadora > 100:
#     descuento = computadora * IVA 
#     print(f"La computadora tuvo un descuento de {IVA}% porque el precio es mayor de 100$, el precio de la computadora es: {computadora:.2f}$ y con el descuento es: {descuento:.2f}$")
# else: 
#     print(f"El precio de la computadora es {computadora:.2f}$")

# print(180*0.25)

nota = int(input("Ingrese la nota del estudiante: ")) 

if nota >= 90: 
    print("A")
elif 80 <= nota <90:
    print("B")
elif 70 <= nota <80:
    print("C")
elif 60 <= nota <70:
    print("D")
else: 
    print("Reprobado")