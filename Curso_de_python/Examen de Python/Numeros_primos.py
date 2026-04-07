#Ingreso un numero 
def exprimo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0:
        return False
    
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2
    return True

print(exprimo(5))
print(exprimo(10))
