import pandas as pd
df = pd.read_csv('GoogleApps.csv')


#1 Muestre el 'Rating' mínimo, promedio, y máximo de aplicaciones de pago y gratuitas ('Type') y redondee a la décima más cercana.
print('\nDatos:')
print(round(df.groupby('Type')['Rating'].agg(['min', 'mean', 'max']), 1))


#2 Muestre el 'Price' mínimo, medio, y máximo de aplicaciones de pago (Type == 'Paid') para # diferentes públicos objetivo ('Content Rating')
print('\nDatos:')
print(df[df['Type'] == 'Paid'].groupby('Content Rating')['Price'].agg(['min', 'median', 'max']))


#3 Agrupar los datos por 'Category' y público objetivo ('Content Rating') como prefiera
#calcule el número máximo de 'Reviews' para cada grupo.
#Compare los resultados para las categorías 'EDUCATION', 'FAMILY, y 'GAME'.
#¿En qué grupo de edad recibió más reseñas la aplicación en la categoría 'EDUCATION'? ¿'FAMILY'? ¿'GAME'?


#Consejo: Puede seleccionar múltiples columnas del DataFrame a la vez usando la siguiente sintaxis:
# df[[<column 1>, <column 2>, <column 3>]]

print('\nDatos:')

temp = df.pivot_table(
  index = 'Content Rating', 
  columns = 'Category', 
  values = 'Reviews', 
  aggfunc = 'max'
)
print(temp[['EDUCATION', 'FAMILY', 'GAME']])


#4 Agrupe las aplicaciones de pago (Type == 'Paid') por 'Category' y por público objetivo ('Content Rating')
#Calcule el número promedio de 'Reviews' para cada grupo
#Tenga en cuenta que algunas celdas en la tabla de resultados tienen el valor "NaN" – Not A Number – en lugar de un número
#Eso significa que no hay aplicaciones en ese grupo.
#Elija los nombres de las categorías que tengan aplicaciones de pago para todos los grupos de edad y ordénelas por orden alfabético.

print('\nDatos:')
print(df[df['Type'] == 'Paid'].pivot_table(
  columns = 'Content Rating', 
  index = 'Category', 
  values = 'Reviews', 
  aggfunc = 'mean'
))


#Tarea de bonificación. Encuentre las categorías de aplicaciones gratuitas (Type == 'Free')
#en qué grupos las aplicaciones no estaban diseñadas para todos los grupos de edad ('Content Rating')
print(df[df['Type'] == 'Free'].pivot_table(
  index = 'Category', 
  columns = 'Content Rating', 
  values = 'Reviews', 
  aggfunc = 'mean'
))