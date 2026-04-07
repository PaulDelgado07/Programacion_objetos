contador = 0 

def incrementar():
    global contador 
    contador =+1
    print(f"Dentro de incrementar, incremenar {contador}")

incrementar()