# Mostrar reporte de ventas: 

def mostrar_reporte_ventas():
    print("Reporte de ventas:")
    try:
        with open('ventas.txt', 'r') as archivo:
            contenido = archivo.readlines()
            if contenido: 
                for i in contenido: 
                    print(i.split())
            else: 
                print("el archivo no hay")
    except FileNotFoundError: 
        print("Archivo no existe. ")

mostrar_reporte_ventas()