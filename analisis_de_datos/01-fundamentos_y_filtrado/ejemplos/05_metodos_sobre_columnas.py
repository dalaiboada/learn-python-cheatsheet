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

# * Formula df['columna'].operacion()

print("\nValor minimo (empleado mayor):\n", df['Edad'].min())
print("\nValor maximo (empleado menor):\n", df['Edad'].max())
print("\nPromedio (Edad promedio):\n", df['Edad'].mean())
print('Cantidad de empleados:\n', df['Edad'].count())
print("\nSuma (Salario total):\n", df['Salario'].sum())

# otros
print("\nDesviacion estandar (Edad):\n", df['Edad'].std())
print("\nMediana (Edad):\n", df['Edad'].median())
print("\nModa (Edad):\n", df['Edad'].mode())
print("\nVarianza (Edad):\n", df['Edad'].var())

# aplicar una función
# * Formula df['columna'].apply(funcion)

# Tener el la longitud del nombre de cada empleado
df['Longitud_Nombre'] = df['Nombre'].apply(len)

print(df)