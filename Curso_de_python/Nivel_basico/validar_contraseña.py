def verificar_contraseña(contrasena):
    #verificar longitud minima (8 caracteres): 
    if len(contrasena) < 8:
        return False 
    
    #verificamos si contiene al menos un numero 
    if not any(char.isdigit() for char in contrasena): 
        return False 
    # verificamos si contiene al menos una mayuscula 
    if not any(char.isdigit() for char in contrasena): 
        return False
    # verificamos si contiene al menos un caracter especial
    especial = "#$%&/()=?¡¡!"

    if not any(char in especial for char in contrasena): 
        return False
    
    #todo si pasa todas las verificaciones, la contraseña es segura.
    return True