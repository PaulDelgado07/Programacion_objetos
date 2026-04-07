import pandas as pd 

# #Crear una serie a partir de una lista
# data = [10, 20, 30, 40, 50]

# serie = pd.Series(data)
# print(serie)

#CREAR una dataFrame a partir de un diccionario
data = {
    'Nombre' : ['Juan', 'Ana', 'Pedro', 'Luis'],
    'edad' : [28, 22, 35, 32],
    'Ciuda' : ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)

mayores_30 = df[df['edad'] > 30]
print(df)
print("\n---Mayores que 30 años---\n",mayores_30)

# datos = "C:/Users/Paul/OneDrive/Desktop/Progrmar/Curso_de_python/Nivel_Avanzado/datos.csv"
# df = pd.read_csv(datos, sep= ";") 


# print(df.head())
