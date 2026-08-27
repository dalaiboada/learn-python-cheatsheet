import pandas as pd

# Cargar el marco de datos
df = pd.read_csv ('GoogleApps.csv')

# ¿Cuál es el nombre de la primera aplicación en el conjunto de datos?
# * Res: Photo Editor & Candy Camera & Grid & ScrapBook
print(df.head(3))


# ¿A qué categoría pertenece la última aplicación del conjunto de datos?
# * Res: LIFESTYLE
print(df.tail(3))

# ¿Cuántas columnas hay en el conjunto de datos?
# ¿Qué tipo de datos se almacenan en cada una de las columnas?
""" 
Reseña (Reviews)
Content Rating(Clasificación de Contenido)
Rating (Clasificación) 
"""
print(df.info())


# Especifique la media aritmética y la mediana del tamaño de la aplicación (Tamaño)
# * Res:  Promedio = 22.77 |  Mediana = 14 
# ¿Cuánto cuesta la aplicación más cara? 
# *Res: 400

# (Extra) Especifique la media aritmética y la mediana del número de instalaciones de aplicaciones (Instalaciones)
# * Res:  Promedio = 8662313 |  Mediana = 100000 
print(df.describe())