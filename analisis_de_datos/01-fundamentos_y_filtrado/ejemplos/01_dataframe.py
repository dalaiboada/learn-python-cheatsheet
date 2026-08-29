import pandas as pd

# 1. Crear un dataframe desde un diccionario
datos = {
    'Nombre': 
        ['Ana', 'Carlos', 'Lucía', 'Mateo', 'Elena'],
    'Departamento': 
        ['Ventas', 'TI', 'TI', 'Ventas', 'Marketing'],
    'Edad': 
        [28, 35, 30, 24, 42],
    'Salario': 
        [3200, 4100, 3800, 2900, 4800]
}

# Crear el DataFrame
df = pd.DataFrame(datos)
print(df)