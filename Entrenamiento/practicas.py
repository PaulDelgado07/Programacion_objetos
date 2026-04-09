"""
 Ejercicio: Analizador de números

Crea un programa que haga lo siguiente:

Pida al usuario ingresar una lista de números separados por comas
Ejemplo:

5,8,2,10,3
Con esos datos, el programa debe:
Mostrar el número mayor
Mostrar el número menor
Calcular el promedio
Mostrar cuántos números son pares
Mostrar cuántos son impares
 Ejemplo esperado
Ingrese números: 5,8,2,10,3

Mayor: 10
Menor: 2
Promedio: 5.6
Pares: 3
Impares: 2
"""
import math 

# rango = int(input("Ingrese cuantas veces desea: "))
numeros=[5,8,2,10,3]

# for i in range(rango):
#     numero = input("Ingrese el numero deseado: ")
#     numeros.append(int(numero))

#numeros mayores 
num_mayor = max(numeros)

#numeros manores 
num_menor = min(numeros)

#numeros pares 
pares = 0
impares = 0

for i in numeros:
    if i % 2==0:
        pares+=1
    else:
        impares+=1


print("Mayor:",num_mayor)
print("Menor:", num_menor)
print("Pares:",pares)
print("Impares:",impares)