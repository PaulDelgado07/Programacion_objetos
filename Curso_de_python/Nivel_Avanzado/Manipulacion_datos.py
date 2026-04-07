import pandas as pd 

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('C:/Users/Paul/OneDrive/Desktop/Progrmar/Curso_de_python/Nivel_Avanzado/denunciasVictimaspgj.csv')
# print(df.head()) #Muestra la cabecera de los dataframe
# print(df.info()) #Muestra la iformacion de todas la cabeceras
# print(df.tail()) #Muestra los 5 ultimos de la data Frame
# print(df.loc[43]) #Muestra iformacion de un solo usuario
# print(df.loc[[2,4,6,7]]) #Muestra informacion de varios usuarios utilizando listas
# print(df.loc[[2,4,6,7],["categoria","sexo", "tipopersona"]])
# print(df["categoria"].unique()) #para ver los vectores unicos de las cabeceras
# print(df.loc[df["categoria"] == "DELITO DE BAJO IMPACTO"])
# print(df.columns) #para ver las listas de las columnas
# print(df.loc[df["sexo"] == "Femenino"].head(10))
# print(df.loc[df["edad"] < 18].head(10))
# delitos_alto_impacto = ["VIOLACIÓN", "SECUESTRO"]
# print(df.loc[df["categoria"].isin(delitos_alto_impacto)].head(10))
#print(df.loc[(df['sexo'] == 'Femenino') & (df['edad'] < 18)].head(10))
# print(df["delito"].sort_values().head(10))
# print(df.sort_values(['sexo', 'edad'], ascending=[True, False]))
# print(df['sexo'].value_counts())

# df_resultado = df.loc[(df['sexo'] == 'Femenino') & (df['edad'] < 18)].head(10)
# df_resultado.to_csv("Data_optenida", index=False)

#Introduccion query 

data = {
    'nombre' : ['Ana', 'Juan ', 'Maria', 'luis', 'Pedro'],
    'edad' : [12, 34, 65, 32, 76],
    'ciudad' : ['Madrid', 'Barcelona', 'Cevilla', 'Madrid', 'Valencia'],
    'Salario' : [30.000, 40.000, 50.000, 60.000, 120.000]
}

df = pd.DataFrame(data)

#print(df.loc[(df['ciudad'] == 'Madrid') & (df['Salario'] >= 30.000)])#metodo grande pero muy bien explisita
#resultado = df.query('ciudad == "Madrid" & Salario >= 30.000') #Metodo más practico 
# V_ciudad = 'Madrid'
# resultado2 = df.query('ciudad == @V_ciudad')
# print(resultado2)
print(df.loc[1])
#print(df.loc[:,['edad']])}
print("________________")
print(df.iloc[0 : 2])
print(df.iloc[0 : 2, 0 : 2])