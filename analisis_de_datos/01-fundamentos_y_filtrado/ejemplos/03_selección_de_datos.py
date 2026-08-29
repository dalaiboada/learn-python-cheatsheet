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

# 1. Seleccionar una columna (devuelve una serie)
print('\nMostrando seleccion de columna:\n')
columna_nombre = df['Nombre']

print(df.Edad) # solo si no tienen espacio
print(columna_nombre)

# 2. Seleccionar varias columnas (devuelve un DataFrame)
print('\nMostrando seleccion de varias columnas:\n')
resumen = df[['Nombre', 'Salario']]

print(resumen)