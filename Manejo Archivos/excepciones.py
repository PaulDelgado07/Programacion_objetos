############################################################
# try:
#     numero_ingresado = int(input("Ingrese un valor: "))
#     resultado = numero_ingresado/2 
# except Exception as valor: 
#     print(valor)
# else: 
#     print("No ocurrió ninguna excepción")
# finally:
#     print("Se terminó la ejecución")
###########################################################
try:
    tipo = False 
    if tipo == True:
        print("El resultado")
except SyntaxError as r:
    print(f"Error de sintaxis {r}")