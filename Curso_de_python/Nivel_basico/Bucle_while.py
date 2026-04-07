"""
while condicion: 
  "bloque de condigo"
"""

# contador = 1 
# while contador <= 5:
#     print(contador)
#     contador += 1

# sum = 0
# n = 1 

# while sum < 20:
#     sum +=n 
#     n +=1

# intentos = 0 

# while intentos < 5: 
#     contraseña = input("Ingresa la contraseña: ")

#     if contraseña == "Paulsincabeza":
#         print("La contraseña es correcta")
#         break 
#     else: 
#         intentos+=1
#         print(f"La contraseña es incorrecta, tienes {intentos} intentos")
# if intentos == 5:
#     print("--Cuenta Bloqueada--")

intentos = 3
while intentos < 4: 
    usuario = input("Ingresa el usuario: ")
    contraseña = input("Ingresa la contraseña: ")
    if usuario == 123 and contraseña == "paulsincabeza":
        print("El usuario y contraseña son correctos. ")
        break 
    else: 
        intentos -=1
        print(f"Usuario o contraseña son incorrectos, Te quedan {intentos} intentos.")
if intentos == 0:
    print("Cuenta Bloqueada")