import pandas as pd
import numpy as np

datos = {
    'Region': ['Norte', 'Norte', 'Norte', 'Sur', 'Sur', 'Sur', 'Este', 'Este'],
    'Tipo': ['Tecnología', 'Muebles', 'Tecnología', 'Muebles', 'Muebles', 'Tecnología', 'Tecnología', 'Muebles'],
    'Vendedor': ['Ana', 'Carlos', 'Ana', 'Luis', 'Elena', 'Luis', 'Sofia', 'Sofia'],
    'Ventas': [1200, 300, 850, 400, 650, 950, 1100, 200],
    'Descuento': [0.10, 0.05, 0.15, 0.00, 0.10, 0.20, 0.05, 0.00],
    'Unidades': [4, 2, 3, 5, 4, 3, 6, 1]
}

df = pd.DataFrame(datos)

print('\nDataFrame:')
print(df)

# Promedio de todas las variables numéricas por Región
print('\nRegion:')

region = df.groupby('Region').mean(numeric_only=True)
print(region)

# Promedio de ventas por Región (Serie)
print('\nVentas por region:')

region_ventas = df.groupby('Region')['Ventas'].mean()
print(region_ventas)

# Varias columnas específicas (devuelve un DataFrame)
print('\nVarias columnas específicas:')

region_ventas_unidades = df.groupby('Region')[['Ventas', 'Unidades']].mean()
print(region_ventas_unidades)

# Varias agrupaciones
print('\nPromedio varias agrupaciones (Region y tipo):')

varias_agrupaciones = df.groupby(['Region', 'Tipo']).mean(numeric_only=True)
print(varias_agrupaciones)


# Varias agrupaciones y una columna especifica
print('\nPromedio Varias agrupaciones (Region y tipo) y una columna especifica (Ventas):')

varias_agrupaciones_columnas = df.groupby(['Region', 'Tipo'])['Ventas'].mean()
print(varias_agrupaciones_columnas)


# Aplicar varios métodos estadísticos sobre la agrupación
# Promedio y mínimo de Unidades por Región
print('\nPromedio y mínimo:')

prom_min_unidades = df.groupby('Region')['Unidades'].agg(['mean', 'min'])
print(prom_min_unidades)


# distintos métodos estadísticos a cada columna: 
# maximo de ventas para cada tipo, la suma de unidades para cada tipo
print('\nDistintas operaciones a cada columna:')

varias_opcs = df.groupby('Tipo').agg({
    'Ventas': 'max',
    'Unidades': 'sum'
})
print(varias_opcs)
