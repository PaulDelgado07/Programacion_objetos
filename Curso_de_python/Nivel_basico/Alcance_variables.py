"""
AMBITO LOCAL 

"""
global_var = 20
def my_fucion():
    local_var=10   #variable local
    print(local_var)

def my_fuction_dos():
    print(global_var)

#my_fuction_dos()

"""
AMBITO GLOBAL 
"""
count = 0 

def incremento_valor():
    global count 
    count +=1

incremento_valor()
print(count)


arreglo = [10, 20, 30]

arreglo.append(40)
print(arreglo)