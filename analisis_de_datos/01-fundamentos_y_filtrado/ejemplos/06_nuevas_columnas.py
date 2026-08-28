import pandas as pd

datos = {
    'Nombre': 
        ['Ana', 'Carlos', 'Lucia', 'Mateo', 'Elena'],
    'Departamento': 
        ['Ventas', 'TI', 'TI', 'Ventas', 'Marketing'],
    'Edad': 
        [28, 35, 30, 28, 42],
    'Salario': 
        [3200, 4100, 3800, 2900, 4800]
}

df = pd.DataFrame(datos)

# Añadir una columna para un bono que será el 10% de su salario
df['Bono'] = df['Salario'] * 0.10

# Añadir una columna que combine el nombre y el departamento
df['Nombre_Depto'] = df['Nombre'] + " - " + df['Departamento']

print(df)