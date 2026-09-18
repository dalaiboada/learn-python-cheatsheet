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

print('\nNULOS (Todos):')
print(df.isnull())

print('\nNULOS (Columna Nombre):')
print(df['Nombre'].isnull())

print('\nCANTIDAD DE NULOS (Todos):')
print(df.isnull().sum())

print('\nCANTIDAD DE NULOS (En Edad):')
print(df['Edad'].isnull().sum())

