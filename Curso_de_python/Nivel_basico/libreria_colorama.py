# colorama
# es una libreria escrita en python que me permite cambiar los colores 
# y el formato de fuente en mis programas de consola

from colorama import Fore, Back, Style, init 

init(autoreset = True)

#cambiar el color del texto 
def ejemplo_colorama():
    print(Fore.RED + "esto es un texto en rojo")
    print(Back.LIGHTMAGENTA_EX + "hola que tal")
    print(Fore.RED + Back.YELLOW + "Esto es una cadena")
    print(Style.BRIGHT + "Texto en negrita")

    print(Fore.WHITE + Back.BLACK + "Texto en blanco sobre fondo negro" + Style.RESET_ALL)

def Menu_opciones(): 
    borde_superior = f"{Fore.BLUE}" + "+" + "-" * 34 + "+ " 
    borde_inferior = f"{Fore.BLUE}" + "+" + "-" * 34 + "+ "

    
    opcciones = [
        f"{Fore.CYAN}{Back.BLACK}"+ "|1. Opción 1                       |",
        f"{Fore.CYAN}{Back.BLACK}"+ "|2. Opción 2                       |",
        f"{Fore.CYAN}{Back.BLACK}"+ "|3. Opción 3                       |"
    ]

    print(borde_superior)

    for i in opcciones:
        print(i)

    print(borde_inferior)
Menu_opciones()

seleccion = (input(f"Ingrese el numero de las opcciones: "))
if seleccion == "1": 
    print(f"{Fore.GREEN}{Back.BLACK}"+"Has seleccionado la opccion 1.")
elif seleccion == "2": 
    print(f"{Fore.MAGENTA}{Back.BLACK}"+"Has seleccionado la opccion 2.")
elif seleccion == "3": 
    print(f"{Fore.BLUE}{Back.BLACK}"+"Has seleccionado la opccion 3.")






