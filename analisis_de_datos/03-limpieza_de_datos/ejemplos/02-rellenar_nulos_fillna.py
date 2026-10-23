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


print('\nTODOS LOS NULOS DEL DATA FRAME:')
df2 = df.fillna(0)
print(df2)


print('\nDATA FRAME CON EDAD RELLLENADA:')
df['Edad'] = df['Edad'].fillna(8)
print(df)


print('\nRELLENAR CON LA EDAD PROMEDIO')
print('Edad promedio: ', df['Edad'].mean())

df['Edad'] = df['Edad'].fillna(df['Edad'].mean())
print(df)