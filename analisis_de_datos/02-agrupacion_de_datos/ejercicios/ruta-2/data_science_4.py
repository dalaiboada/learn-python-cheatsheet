import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Muestre el 'Rating' mínimo, promedio, y máximo de aplicaciones de pago y gratuitas ('Type') y redondee a la décima más cercana.

# 2 Muestre el 'Price' mínimo, medio, y máximo de aplicaciones de pago (Type == 'Paid') para 
# diferentes públicos objetivo ('Content Rating')

# 3 Agrupe los datos por 'Category' y público objetivo ('Content Rating') como prefiera
# calcule el número máximo de 'Reviews' para cada grupo.
# Comparte los resultados para las categorías 'EDUCATION', 'FAMILY, y 'GAME'.
# ¿En qué grupo de edad recibió más reseñas la aplicación en la categoría 'EDUCATION'? ¿'FAMILY'? ¿'GAME'?
# Consejo: Puede seleccionar múltiples columnas del DataFrame a la vez usando la siguiente sintaxis:
# df[[<column 1>, <column 2>, <column 3>]]


# 4 Agrupe las aplicaciones de pago (Type == 'Paid') por 'Category' y por público objetivo ('Content Rating')
# Calcule el número promedio de 'Reviews' para cada grupo
# Tenga en cuenta que algunas celdas en la tabla de resultados tienen el valor "NaN" – Not A Number – en lugar de un número
# Eso significa que no hay aplicaciones en ese grupo.
# Elija los nombres de las categorías que tengan aplicaciones de pago para todos los grupos de edad y ordénelas por orden alfabético.

# Tarea de bonificación Encuentre las categorías de aplicaciones gratuitas (Type == 'Free') 
# en las cuales las aplicaciones no estaban diseñadas para todos los grupos de edad ('Content Rating')

