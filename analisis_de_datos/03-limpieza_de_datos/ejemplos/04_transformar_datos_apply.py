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

#df['columna'].apply(funcion)

def clasificar_nota(nota):
    if nota >= 9:
        return 'Excelente'
    elif nota >= 7:
        return 'Bien'
    else:
        return 'Necesita mejorar'


print('\nDATA FRAME CON NOTA CLASIFICADA:')
df['Nota'] = df['Nota'].apply(clasificar_nota)
print(df)