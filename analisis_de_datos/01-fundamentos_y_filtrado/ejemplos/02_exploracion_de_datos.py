import pandas as pd

datos = {
    'Nombre': 
        ['Ana', 'Carlos', 'Lucia', 'Mateo', 'Elena'],
    'Departamento': 
        ['Ventas', 'TI', 'TI', 'Ventas', 'Marketing'],
    'Edad': 
        [28, 35, 30, 24, 42],
    'Salario': 
        [3200, 4100, 3800, 2900, 4800]
}

df = pd.DataFrame(datos)

print('\nMostrando el DataFrame completo:\n')
print(df)

print('\nMostrando primeras filas DataFrame df.head():\n')
print(df.head(2))

print('\nMostrando ultimas filas DataFrame df.tail():\n')
print(df.tail(2))

print('\nMostrando informacion del DataFrame df.info():\n')
informacion = df.info()

print(informacion)

print('\nMostrando estadisticas del DataFrame df.describe():\n')
print(df.describe())

print('\nMostrando tipos de datos de columna con df.dtypes:\n')
print(df.dtypes)

print('\nMostrando numero de filas y columnas con df.shape:\n')
print(df.shape)

print('\nMostrando columnas con df.columns:\n')
print(df.columns)