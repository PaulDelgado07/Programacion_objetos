while True:
    try:
        entrada = input("Ingrese un numero entero (o 'salir' para terminar): ")
        
        # Una forma elegante de salir
        if entrada.lower() == 'salir':
            break
            
        numero = int(entrada)
        
        # Lógica de Par / Impar
        if numero % 2 == 0:
            print(f"El número {numero} es PAR")
        else:
            print(f"El número {numero} es IMPAR")
        
        # Preguntar siempre si desea continuar
        respuesta = input("¿Quieres probar otro número? (S/N): ").upper()
        if respuesta == 'N':
            print("-- Programa cerrando --")
            break
            
    except ValueError:
        print(" Error: Por favor, ingrese un número entero válido.")

