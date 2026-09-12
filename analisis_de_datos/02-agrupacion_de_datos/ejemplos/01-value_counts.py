# Contar frecuencias
# df['col'].value_counts()

import numpy as np
import pandas as pd

data = {
    'Producto': [
        'Manzana',
        'Pera',
        'Manzana',
        'Naranja',
        'Manzana',
        np.nan,
        'Pera',
    ],
    'Precio': [10, 12, 10, 20, 10, 25, 15],
}
df = pd.DataFrame(data)

print('\nDatos:')
print(df)

print('\nFrecuencia de categorías de productos:')
print(df['Producto'].value_counts())

print('\nFrecuencia de categorías de productos (%):')
print(df['Producto'].value_counts(normalize=True) * 100)

print('\nFrecuencia de categorías de productos incluyendo nulos:')
print(df['Producto'].value_counts(dropna=False))

print('\nFrecuencia de múltiples columnas:')
print(df[['Producto', 'Precio']].value_counts())
