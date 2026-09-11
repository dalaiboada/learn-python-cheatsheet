import pandas as pd

data = {
    'Estudiante': ['Ana', 'Ana', 'Carlos', 'Carlos', 'Ana', 'Ana', 'Carlos', 'Carlos'],
    'Materia': ['Matemáticas', 'Historia', 'Matemáticas', 'Historia', 'Matemáticas', 'Historia', 'Matemáticas', 'Historia'],
    'Periodo': ['P1', 'P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P2'],
    'Nota': [18, 15, 12, 14, 20, 16, 15, 13]
}

df = pd.DataFrame(data)

print('\nDatos:')
print(df)

print('\nTabla dinamica:')
tabla_dinamica = df.pivot_table(
    index='Estudiante',     # Filas
    columns='Periodo',      # Columnas
    values='Nota',          # Dato a resumir (calcular)
    aggfunc='mean'          # Función de agregación (promedio)
)

print(tabla_dinamica)
