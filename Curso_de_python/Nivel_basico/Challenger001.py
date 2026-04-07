"""
001 Calcular el precio total de un producto co IGV


#PRECIO_SIN_IGV = 100
#IGV = 0.18 
 
#precio_con_igv = PRECIO_SIN_IGV*(1+IGV)
#print(f"Precio con IGV: {precio_con_igv:.2f}")

nombre_producto = input("INgrese el nombre del producto: ")
precio_producto =float(input("Ingrese el precio del producto: "))
cantidad_producto = int(input("Ingrese la cantidad del producto: "))
total_a_pagar = precio_producto*cantidad_producto
igv_a_pagar = total_a_pagar * 0.18 
total_neto=total_a_pagar+igv_a_pagar
print(f"El nombre del producto {nombre_producto}, tiene un total de ${total_neto:.2f} el IGV a pagar es: {igv_a_pagar:.2f}")
"""

"""
002 - Calcular salario semanal de un trabajador

nombre_trabajador = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
tarifa_horas = float(input("Ingrese la tarifa por horas: "))
salario_diario = tarifa_horas*horas_trabajadas 

print(f"El salario del trabajador {nombre_trabajador} es: ${salario_diario:.2f} ")

"""

"""
003 - Promedio de notas de los alumnos

nombre_alumno = input("Ingrese el nombre del alumno: ")
notas = [10, 8, 9]
for i in notas:
    print(f"nota: {i}")
    promedio = sum(notas)/len(notas)
print(f"El promedio del alumno {nombre_alumno} es: {promedio}")
"""
cantidad = int(input("Ingresa la cantidad de alumnos: "))

for i in range(cantidad): 
    nombre = input("Ingresa el nombre del alumno: ")
    cantidad_notas = int(input("Ingrese la cantidad de notas: "))
    calificaciones = [] 
    for j in range(cantidad_notas):
        nota = float(input("Ingrese la nota: "))
        calificaciones.append(nota)

promedio = sum(calificaciones)/len(calificaciones)
print (f"El promedio del estudiante {nombre} es de: {promedio}")
