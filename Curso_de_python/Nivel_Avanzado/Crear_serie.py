#Crear una serie a partir de una lista. - 
import pandas as pd 

# serie = pd.Series([10, 20, 30, 40, 50], name = "Lista de serie")
# print(serie)

diccionario = { 
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4, 
}

serie = pd.Series(diccionario, name = "Series")
print(serie)