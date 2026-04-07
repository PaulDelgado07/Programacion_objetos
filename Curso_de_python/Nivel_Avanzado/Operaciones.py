import math 
import pandas as pd 
#sumar 
serie1 = pd.Series([10, 20, 30])
serie2 = pd.Series([1, 2 ,3])


# def suma_series(objeto1, objeto2):
#     if suma_series is None:
#         return f"No existe objetos"
#     else: 
#         return objeto1 + objeto2
    
# print(suma_series(serie1, serie2))

#Suma de operaciones en dataFrame

df1 = pd.DataFrame({
    'A' : [1, 2, 3],
    'B' : [4, 5, 6]
})

df2 = pd.DataFrame({
    'A' : [10, 20, 30],
    'B' : [40, 50, 60]
})

def sumarDataFrame(funcion1, funcion2): 
    return funcion1 + funcion2

print(sumarDataFrame(df1,df2))