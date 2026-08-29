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

# * Formula: df_resultante = df[condicion]

# eg. 1: Mostrar empleados (filas) que trabajan en el departamento de TI
print('\nMostrando empleados que trabajan en el departamento de TI:\n')
columna_departamento = df['Departamento']
df_departamento_TI = df[columna_departamento == 'TI']

# print(df[df['Departamento'] == 'TI']) # otra forma de hacerlo
print(df_departamento_TI)

# eg. 2: Mostrar empleados (filas) que tienen un salario mayor a 3500
print('\nMostrando empleados que tienen un salario mayor a 3500:\n')
print(df[df['Salario'] > 3500])

# Condiciones múltiples
# |(o)   & (y) 
# * Formula: df_resultante = df[(condicion1) & (condicion2)]

# eg. 3: Mostrar empleados (filas) que trabajan en el departamento de TI y tienen un salario mayor a 3500
print('\nMostrando empleados que trabajan en el departamento de TI y tienen un salario mayor a 3500:\n')
print(df[(df['Departamento'] == 'TI') & (df['Salario'] > 3500)])