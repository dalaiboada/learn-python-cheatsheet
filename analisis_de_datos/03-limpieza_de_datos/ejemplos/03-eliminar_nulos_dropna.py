import pandas as pd

datos = {
    'Nombre': ['Ana', 'Carlos', 'Lucia', 'Mateo', 'Elena'],
    'Edad': [15, None, 14, 16, None],
    'Nota': [8.5, 9.0, None, 7.5, 10.0],
    'Ciudad': ['Miami', 'Madrid', None, 'Miami', 'Madrid']
}

df = pd.DataFrame(datos)

print('\nDATA FRAME:')
print(df)

print('\nCOLUMNAS:')
print(df.info())


print('\nDATA FRAME SIN NULOS:')
nuevo_df = df.dropna()
print(nuevo_df)

# dropna puede eliminar FILAS o COLUMNAS
# predeterminado -> Filas axis=0
# columnas -> axis=1

print('\nDATA FRAME SIN COLUMNAS NULAS:')
nuevo_df2 = df.dropna(axis=1)
print(nuevo_df2)


# A veces solo queremos eliminar una columna si tiene cualquiera nulo o TODOS nulos
# eso lo controlamos con how, por defecto how='any'

# how = 'any' -> Elimina si tiene AL MENOS un nulo
# how = 'all' -> Elimina si tiene TODOS nulos

print('\nELIMINAR TODA LA COLUMNA SOLO SI TODAS SON NULOS:')
nuevo_df3 = df.dropna(how='all', axis=1)
print(nuevo_df3)


# Podemos decirle a dropna cuál columna revisar para eliminar 
# dropna(subset=['col'])

print('\nELIMINAR TODA LA FILA SOLO SI FALTA EN EDAD:')
nuevo_df4 = df.dropna(subset=['Edad'])
print(nuevo_df4)
