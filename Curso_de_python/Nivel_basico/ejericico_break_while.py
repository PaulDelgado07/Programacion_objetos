"""
Hasta que ingrese el numero 0 

"""

# while True: 
#     numero = int(input("Introduce un numero (0 para salir): "))
#     if numero == 0:
#         print("Saliendo del bucle...")
#         break
#     print(f"Ingresaste {numero}")

#solicitar al usuario para si el numero es negativo lo voy a ignorar
#solo imprimire numeros positivos.
 
while True: 
    numero = int(input("Ingrese un numero: "))
    if numero < 0:
        print("Numero ignorado")
        continue
    elif numero == 0:
        print("Saiendo del programa...")
        break
    else: 
        print(f"Tu mumero es: {numero}")



