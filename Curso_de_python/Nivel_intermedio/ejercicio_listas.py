# frutas = list()

# while True: 
#     nueva_fruta = input("Ingrese una nueva fruta: ")
#     if nueva_fruta in frutas: 
#         posicion = frutas.index(nueva_fruta)
#         print(f"La fruta ya existe y se encuentra en la posicion {posicion}.")
#         respuesta = input("desea continuar: ")
#         if respuesta == "no": 
#             break
#     else: 
#         frutas.append(nueva_fruta)
#         print(frutas)


# frutas = ["manzana", "pera", "guineo", "kiwi"]

# for index, nombre in enumerate(frutas, start= 1): 
#     print(f"{index}. {nombre}")

# from colorama import Fore, Back, Style, init

# init()

# mascotas = list()

# while True: 
#     nueva_mascota = input("Ingresa el nombre de la nueva mascota: ")
#     if nueva_mascota in mascotas: 
#         posicion = mascotas.index(nueva_mascota)
#         print(f"La mascota ya está registrada en la posicion {posicion}.")
#         cuestion = input("Usted desea continuar: ")
#         if cuestion == "no":
#             print("Gracias, hasta la proxima.")
#             break
#     else: 
#         mascotas.append(nueva_mascota)
#         print(mascotas)

# print(Fore.YELLOW + Back.MAGENTA +"U na lista mas ordenada: "+ Style.RESET_ALL)
# for index, nombre in enumerate(mascotas, start= 1): 
#     print(f"{index}. {nombre}")


from colorama import Fore, Back, Style, init

init()
mascotas = list()
while True: 
    nueva_mascota = input("Ingrese una nueva mascota: ")
    if nueva_mascota in mascotas: 
        posicion = mascotas.index(nueva_mascota)
        print(f"Esta mascota ya existe y està en la posición: {posicion}") 
        respuesta = input("Ingrese (No) si ya no desea ingresar más mascotas")
        if respuesta == "No": 
            print("Gracias, Programa cancelado.")
            break
    else: 
        mascotas.append(nueva_mascota)
        print(mascotas)

print(Fore.BLACK+Back.BLUE+ f"Lista de mascota ordenada."+ Style.RESET_ALL)
for index, nombre in enumerate(mascotas, start=1): 
    print(f"{index}. {nombre}")